import pandas as pd
import matplotlib.pyplot as plt
plt.ion()  # Modo interactivo

# ============================================
# ANÁLISIS DE DATOS DE AGUACATES
# ============================================

# Cargar el archivo CSV
data = pd.read_csv("avocado.csv")

print("=" * 70)
print("         ANÁLISIS DE DATOS DE AGUACATES")
print("=" * 70)

# ============================================
# 1. OBTENER FILAS Y COLUMNAS
# ============================================
print("\n1️⃣  FILAS Y COLUMNAS DEL CONJUNTO DE DATOS\n")
filas = data.shape[0]
columnas = data.shape[1]

print(f"   📊 Número de filas: {filas}")
print(f"   📊 Número de columnas: {columnas}")
print(f"   📊 Dimensiones totales: {data.shape}")

# ============================================
# 2. Muestrar los primeros 100 registros
# ============================================
print("\n" + "=" * 70)
print("2️⃣  PRIMEROS 100 REGISTROS")
print("=" * 70)
print(data.head(100))

# ============================================
# 3. Muestrar los últimos 20 registros
# ============================================
print("\n" + "=" * 70)
print("3️⃣  ÚLTIMOS 20 REGISTROS")
print("=" * 70)
print(data.tail(20))

# ============================================
# 4. PRECIO MÍNIMO, MÁXIMO Y PROMEDIO
# ============================================
print("\n" + "=" * 70)
print("4️⃣  ESTADÍSTICAS DEL PRECIO DEL AGUACATE")
print("=" * 70)

precio_minimo = data['AveragePrice'].min()
precio_maximo = data['AveragePrice'].max()
precio_promedio = data['AveragePrice'].mean()

print(f"\n   💰 Precio Mínimo:   ${precio_minimo:.2f}")
print(f"   💰 Precio Máximo:   ${precio_maximo:.2f}")
print(f"   💰 Precio Promedio: ${precio_promedio:.2f}")

print("\n   📈 Estadísticas completas:")
print(data['AveragePrice'].describe())

# ============================================
# 5. GRÁFICO SCATTER PARA 3 REGIONES
# ============================================
print("\n" + "=" * 70)
print("5️⃣  GRÁFICO DE DISPERSIÓN (SCATTER PLOT)")
print("=" * 70)

# Muestra todas las regiones disponibles
print("\n   🌎 Regiones disponibles en el dataset:\n")
regiones_unicas = data['region'].unique()
print(f"   Total de regiones diferentes: {len(regiones_unicas)}\n")

# Muestra las primeras 20 regiones
print("   Primeras 20 regiones (ELIGE 3 DE AQUÍ):")
for i, region in enumerate(regiones_unicas[:20], 1):
    cantidad = len(data[data['region'] == region])
    print(f"   {i:2d}. {region:30s} ({cantidad} registros)")


# ============================================
# Define las regiones a analizar 
# ============================================

region1 = 'Albany'      
region2 = 'WestTexNewMexico'       
region3 = 'Charlotte'           

# ============================================
# CREAR SUBCONJUNTOS DE DATOS
# ============================================
datos_region1 = data[data['region'] == region1]
datos_region2 = data[data['region'] == region2]
datos_region3 = data[data['region'] == region3]

# Verifica que encontró datos
print(f"\n   ✅ Datos para '{region1}': {len(datos_region1)} registros")
print(f"   ✅ Datos para '{region2}': {len(datos_region2)} registros")
print(f"   ✅ Datos para '{region3}': {len(datos_region3)} registros")

# ============================================
# Crea el grafico
# ============================================
if len(datos_region1) > 0 or len(datos_region2) > 0 or len(datos_region3) > 0:
    print("\n   📊 Generando gráfico...")
    
    # Crea figura
    fig = plt.figure(figsize=(14, 8))
    ax = plt.subplot()
    
    # Grafica cada región con diferentes colores
    if len(datos_region1) > 0:
        datos_region1.plot(x='year', y='AveragePrice', kind='scatter', 
                          color='red', label=region1, ax=ax, alpha=0.6, s=40)
    
    if len(datos_region2) > 0:
        datos_region2.plot(x='year', y='AveragePrice', kind='scatter', 
                          color='green', label=region2, ax=ax, alpha=0.6, s=40)
    
    if len(datos_region3) > 0:
        datos_region3.plot(x='year', y='AveragePrice', kind='scatter', 
                          color='blue', label=region3, ax=ax, alpha=0.6, s=40)
    
    # Personaliza el gráfico
    plt.title('Precio Promedio de Aguacate por Año en 3 Regiones', 
              fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('Año', fontsize=14, fontweight='bold')
    plt.ylabel('Precio Promedio ($)', fontsize=14, fontweight='bold')
    plt.legend(title='Regiones', fontsize=12, title_fontsize=13)
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Ajusta diseño y muestra
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(0.1)
    input("\n   ⏸️  Presiona ENTER para cerrar el gráfico y continuar...")
    plt.close()
    
    print("   ✅ ¡Gráfico mostrado!")
else:
    print("\n   ⚠️  ERROR: No se encontraron datos para las regiones seleccionadas.")
    print("   Por favor verifica los nombres de las regiones.")

# ============================================
# FIN DEL ANÁLISIS
# ============================================
print("\n" + "=" * 70)
print("         ✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
print("=" * 70)
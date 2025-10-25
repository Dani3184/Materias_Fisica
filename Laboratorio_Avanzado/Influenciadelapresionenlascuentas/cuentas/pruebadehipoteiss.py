import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import poisson, kstest
import warnings
warnings.filterwarnings('ignore')

# Nombre del archivo de datos
nombre_archivo = 'estadisticas_5min.csv'

try:
    # Leer el archivo
    df = pd.read_csv(nombre_archivo)
    
    # Pedir al usuario los umbrales
    print("=" * 60)
    print("SELECCIÓN DE UMBRALES")
    print("=" * 60)
    min_val = 200
    max_val = 1000
    # min_val = float(input("Umbral mínimo de media: ") or "0")
    # max_val = float(input("Umbral máximo de media: ") or str(df['Media'].max()))
    
    # Filtrar datos por umbrales
    datos_filtrados = df[(df['Media'] >= min_val) & (df['Media'] <= max_val)]['Media']
    
    print(f"\nDatos después de filtrar: {len(datos_filtrados)} de {len(df)}")
    
    if len(datos_filtrados) == 0:
        print("No hay datos en el rango especificado.")
        exit()
    
    datos = datos_filtrados
    
    print("=" * 60)
    print("PRUEBA DE HIPÓTESIS PARA DISTRIBUCIÓN DE POISSON")
    print("=" * 60)
    
    # 1. Estadísticas descriptivas básicas
    print("ESTADÍSTICAS DESCRIPTIVAS:")
    print(f"Número de datos: {len(datos)}")
    print(f"Media: {datos.mean():.4f}")
    print(f"Varianza: {datos.var():.4f}")
    print(f"Desviación estándar: {datos.std():.4f}")
    print(f"Ratio varianza/media: {datos.var()/datos.mean():.4f}")
    print(f"Mínimo: {datos.min():.4f}")
    print(f"Máximo: {datos.max():.4f}")
    
    # 2. Gráficos principales
    plt.figure(figsize=(12, 5))
    
    # Gráfico 1: Histograma comparativo
    plt.subplot(1, 2, 1)
    n_obs, bins, patches = plt.hist(datos, bins=30, alpha=0.7, color='skyblue', 
                                  edgecolor='black', density=True, label='Datos observados')
    
    # Distribución Poisson teórica
    lambda_poisson = datos.mean()
    x = np.arange(max(0, int(datos.min())), int(datos.max()) + 1)
    y_poisson = poisson.pmf(x, lambda_poisson)
    
    plt.plot(x, y_poisson, 'r-', linewidth=2, label=f'Poisson(λ={lambda_poisson:.2f})')
    plt.title('Comparación con Distribución Poisson')
    plt.xlabel('Media de cuentas')
    plt.ylabel('Densidad de probabilidad')
    plt.legend()
    plt.grid(alpha=0.3)
    
    # Gráfico 2: Media vs Varianza
    plt.subplot(1, 2, 2)
    plt.scatter(datos.mean(), datos.var(), color='blue', s=100, alpha=0.7)
    plt.plot([datos.min(), datos.max()], [datos.min(), datos.max()], 'r--', 
             label='Línea Poisson (media = varianza)')
    plt.xlabel('Media')
    plt.ylabel('Varianza')
    plt.title('Media vs Varianza')
    plt.legend()
    plt.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # 3. Prueba de Kolmogorov-Smirnov (la más robusta)
    print("\n" + "=" * 60)
    print("PRUEBA KOLMOGOROV-SMIRNOV")
    print("=" * 60)
    
    ks_stat, p_value_ks = kstest(datos, 'poisson', args=(lambda_poisson,))
    print(f"Estadístico KS: {ks_stat:.4f}")
    print(f"Valor p: {p_value_ks:.4e}")
    
    alpha = 0.05
    if p_value_ks < alpha:
        print("CONCLUSIÓN: Se rechaza H0 - Los datos NO siguen una distribución Poisson")
    else:
        print("CONCLUSIÓN: No se puede rechazar H0 - Los datos podrían seguir una distribución Poisson")
    
    # 4. Test de dispersión (el más importante para Poisson)
    print("\n" + "=" * 60)
    print("TEST DE DISPERSIÓN")
    print("=" * 60)
    
    dispersion_index = datos.var() / datos.mean()
    print(f"Índice de dispersión (varianza/media): {dispersion_index:.4f}")
    
    if dispersion_index > 1.2:
        print("❌ Los datos están SOBREDISPERSOS (varianza > media)")
        print("   - Típico de distribuciones como Binomial Negativa")
    elif dispersion_index < 0.8:
        print("❌ Los datos están SUBDISPERSOS (varianza < media)")
        print("   - Poco común en datos de conteo")
    elif 0.9 <= dispersion_index <= 1.1:
        print("✅ Los datos tienen dispersión Poisson (varianza ≈ media)")
    else:
        print("⚠️  Los datos tienen dispersión cercana a Poisson")
    
    # 5. Resumen final y recomendación
    print("\n" + "=" * 60)
    print("RESUMEN FINAL Y RECOMENDACIÓN")
    print("=" * 60)
    print(f"Media muestral (λ estimado): {lambda_poisson:.4f}")
    print(f"Varianza muestral: {datos.var():.4f}")
    print(f"Ratio varianza/media: {dispersion_index:.4f}")
    print(f"Valor p (Kolmogorov-Smirnov): {p_value_ks:.4e}")
    
    # Evaluación final
    if 0.9 <= dispersion_index <= 1.1 and p_value_ks > 0.05:
        print("\n✅ FUERTE EVIDENCIA: Los datos siguen una distribución Poisson")
    elif 0.8 <= dispersion_index <= 1.2 and p_value_ks > 0.05:
        print("\n⚠️  EVIDENCIA MODERADA: Los datos podrían seguir una distribución Poisson")
    else:
        print("\n❌ EVIDENCIA EN CONTRA: Los datos NO siguen una distribución Poisson")
        
        if dispersion_index > 1.2:
            print("   - Recomendación: Usar distribución Binomial Negativa")
            print("   - Razón: Sobredispersión significativa")
        elif dispersion_index < 0.8:
            print("   - Recomendación: Investigar causas de subdispersión")
            print("   - Razón: Subdispersión inusual para datos de conteo")
        else:
            print("   - Recomendación: La prueba KS rechaza la distribución Poisson")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró.")
except ValueError:
    print("Error: Por favor ingrese valores numéricos válidos para los umbrales.")
except Exception as e:
    print(f"Error: {str(e)}")
import pandas as pd
import numpy as np
from scipy.stats import kstest, poisson
import matplotlib.pyplot as plt

# Nombre del archivo de datos (asegúrate de que esté en la misma carpeta)
archivo_datos = 'estadisticas_5min.csv'

# --- Definir los umbrales para filtrar los datos ---
# Los datos de la columna 'Media' deben estar entre estos dos valores
umbral_min = 200   # Puedes cambiar este valor según tu necesidad
umbral_max = 1000  # Puedes cambiar este valor según tu necesidad

try:
    # Cargar los datos desde el archivo CSV
    df = pd.read_csv(archivo_datos)
    
    # Limpiar los nombres de las columnas de espacios en blanco
    df.columns = df.columns.str.strip()

    # --- Filtrar los datos con base en los umbrales ---
    df_filtrado = df[(df['Media'] >= umbral_min) & (df['Media'] <= umbral_max)]
    
    # Extraer los datos de la columna 'Media' del DataFrame filtrado
    datos_muestra = df_filtrado['Media'].values
    
    # Asegurarse de que hay datos válidos para procesar
    if len(datos_muestra) == 0:
        print(f"Error: No se encontraron datos que estén en el rango de {umbral_min} a {umbral_max}.")
    else:
        # Estimar el parámetro lambda (media) de la distribución de Poisson a partir de la muestra
        lambda_estimado = np.mean(datos_muestra)
        
        # Redondear los datos de la muestra a números enteros, ya que la distribución de Poisson es discreta
        datos_muestra_int = np.round(datos_muestra).astype(int)

        # Realizar la prueba de Kolmogorov-Smirnov
        estadistico_ks, valor_p = kstest(datos_muestra_int, 'poisson', args=(lambda_estimado,))

        print(f"Análisis realizado con datos en el rango de {umbral_min} a {umbral_max} cuentas.")
        print(f"Número de datos filtrados: {len(datos_muestra)}")
        print("-" * 30)
        print(f"Estadístico de la prueba K-S: {estadistico_ks:.4f}")
        print(f"Valor p: {valor_p:.4f}")

        # --- Interpretación de los Resultados ---
        umbral_significancia = 0.05
        if valor_p < umbral_significancia:
            print(f"\nResultado: El valor p es menor que {umbral_significancia}.")
            print("Se rechaza la hipótesis nula. Los datos filtrados probablemente NO siguen una distribución de Poisson.")
        else:
            print(f"\nResultado: El valor p es mayor o igual que {umbral_significancia}.")
            print("No hay evidencia suficiente para rechazar la hipótesis nula.")
            print("Los datos filtrados PODRÍAN seguir una distribución de Poisson.")
            
        # Opcional: Visualización para confirmar el resultado
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

        # Histograma de los datos de la muestra
        bins = np.arange(np.min(datos_muestra_int) - 0.5, np.max(datos_muestra_int) + 1.5)
        ax1.hist(datos_muestra, bins=bins, density=True, alpha=0.6, label='Datos de la Muestra')
        ax1.set_title('Histograma de los Datos')
        ax1.set_xlabel('Valor de Cuentas')
        ax1.set_ylabel('Frecuencia Normalizada')
        ax1.grid(axis='y', linestyle='--')

        # Distribución de Poisson teórica
        x = np.arange(np.min(datos_muestra_int), np.max(datos_muestra_int) + 1)
        pmf_poisson = poisson.pmf(x, mu=lambda_estimado)
        ax1.plot(x, pmf_poisson, 'ro-', label=f'Distribución de Poisson (λ={lambda_estimado:.2f})')
        ax1.legend()

        # Visualización de la CDF
        ecdf = np.cumsum(np.histogram(datos_muestra_int, bins=bins, density=True)[0])
        poisson_cdf = poisson.cdf(x, mu=lambda_estimado)
        ax2.plot(x, poisson_cdf, 'ro-', label='CDF Teórica de Poisson')
        ax2.plot(np.sort(datos_muestra_int), np.linspace(0, 1, len(datos_muestra_int), endpoint=False), 'b-', label='ECDF de la Muestra')
        ax2.set_title('Funciones de Distribución Acumulada (CDF)')
        ax2.set_xlabel('Valor de Cuentas')
        ax2.set_ylabel('Probabilidad Acumulada')
        ax2.legend()
        ax2.grid(linestyle='--')

        plt.suptitle("Prueba de Kolmogorov-Smirnov para la Distribución de Poisson")
        plt.tight_layout(rect=[0, 0, 1, 0.96])
        plt.savefig("pruebKS2.jpg")
        plt.show()

except FileNotFoundError:
    print(f"Error: El archivo '{archivo_datos}' no fue encontrado.")
except KeyError:
    print(f"Error: La columna 'Media' no fue encontrada en el archivo '{archivo_datos}'.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
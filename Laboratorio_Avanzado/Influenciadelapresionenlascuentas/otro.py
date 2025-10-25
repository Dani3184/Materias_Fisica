import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Nombre del archivo donde están los datos
nombre_archivo = 'data.txt'

# Definir el umbral máximo de conteos
UMBRAL_MAXIMO = 140

try:
    # Leer los datos directamente desde el archivo
    df = pd.read_csv(
        nombre_archivo,
        sep=r'\s+',
        header=None,
        names=['fecha', 'hora', 'conteos']
    )

    # Convertir las columnas de fecha y hora en un solo objeto de tipo datetime
    df['timestamp'] = pd.to_datetime(df['fecha'] + ' ' + df['hora'])
    
    # ---
    # Aplicar el umbral máximo para filtrar los datos
    # ---
    df_filtrado = df[df['conteos'] <= UMBRAL_MAXIMO].copy()
    
    print(f"Datos originales: {len(df)} registros")
    print(f"Datos filtrados (<= {UMBRAL_MAXIMO}): {len(df_filtrado)} registros\n")

    # Establecer el 'timestamp' como índice del DataFrame filtrado
    df_filtrado = df_filtrado.set_index('timestamp')

    # ---
    # 1. Generar el histograma de los conteos filtrados
    # ---
    print("Generando el histograma con los datos filtrados...")
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))

    sns.histplot(df_filtrado['conteos'], kde=True, bins=10, color='purple', alpha=0.7)
    plt.title(f'Distribución de Conteos de Rayos Cósmicos (Umbral <= {UMBRAL_MAXIMO}) 🔭', fontsize=16)
    plt.xlabel('Número de Conteos', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

    # ---
    # 2. Calcular la media de conteos cada 5 minutos usando los datos filtrados
    # ---
    print("\nCalculando la media de conteos en intervalos de 5 minutos con los datos filtrados...")
    medias_por_intervalo = df_filtrado['conteos'].resample('5T').mean()

    # Eliminar los NaN si hay intervalos sin datos
    medias_por_intervalo = medias_por_intervalo.dropna()
    
    print(medias_por_intervalo.to_string())

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    print("Asegúrate de que el archivo esté en la misma carpeta que el script.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
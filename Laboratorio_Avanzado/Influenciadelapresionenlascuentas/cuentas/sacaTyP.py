import pandas as pd
import os

# Nombre del archivo de entrada
archivo_entrada = 'ambient-weather-20250829-20250901.csv'

# Nombre del archivo de salida
archivo_salida = 'temperatura_presion_extraida.csv'

# Columnas de interés
columnas_deseadas = ['Date', 'Outdoor Temperature (°C)', 'Absolute Pressure (hPa)']

try:
    # Cargar el archivo CSV en un DataFrame
    df = pd.read_csv(archivo_entrada)

    # Verificar si las columnas deseadas existen
    if not all(col in df.columns for col in columnas_deseadas):
        missing_cols = [col for col in columnas_deseadas if col not in df.columns]
        print(f"Error: El archivo no contiene las columnas necesarias. Faltan: {missing_cols}")
    else:
        # Seleccionar solo las columnas de interés
        df_extraido = df[columnas_deseadas]

        # Guardar el DataFrame extraído en un nuevo archivo CSV
        df_extraido.to_csv(archivo_salida, index=False)

        print(f"Datos extraídos con éxito. El archivo '{archivo_salida}' ha sido creado.")
        
        # Opcional: mostrar las primeras filas del nuevo archivo para verificar
        print("\nPrimeras filas del nuevo archivo:")
        print(df_extraido.head())

except FileNotFoundError:
    print(f"Error: El archivo '{archivo_entrada}' no se encontró en la carpeta actual.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
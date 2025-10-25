import pandas as pd

# Nombre del archivo de entrada
archivo_entrada = 'temperatura_presion_extraida.csv'

# Nombre del archivo de salida
archivo_salida = 'datos_ambientales_ordenados.csv'

try:
    # Leer el archivo CSV
    df = pd.read_csv(archivo_entrada)

    # Convertir la columna 'Date' a un formato de fecha y hora
    df['Date'] = pd.to_datetime(df['Date'])

    # Extraer y renombrar las columnas de interés
    # Se renombra para que sea más fácil de usar en análisis posteriores
    df.rename(columns={
        'Absolute Pressure (hPa)': 'Dato_Presion',
        'Outdoor Temperature (°C)': 'Dato_Temp'
    }, inplace=True)
    
    # Seleccionar las columnas relevantes y ordenar por fecha
    df_ordenado = df[['Date', 'Dato_Presion', 'Dato_Temp']].sort_values('Date').copy()
    
    # Guardar el DataFrame ordenado en un nuevo archivo CSV
    df_ordenado.to_csv(archivo_salida, index=False)

    print(f"El archivo '{archivo_salida}' ha sido creado y ordenado correctamente.")
    print("\nPrimeras filas del nuevo archivo:")
    print(df_ordenado.head())

except FileNotFoundError:
    print(f"Error: El archivo '{archivo_entrada}' no se encontró. Asegúrese de que el archivo esté en la misma carpeta que el script.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
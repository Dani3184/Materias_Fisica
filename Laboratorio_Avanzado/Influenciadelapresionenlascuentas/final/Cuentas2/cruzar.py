import pandas as pd

# --- 1. Cargar los datos de los dos archivos ---
try:
    # Cargar el archivo de meteorología (formato CSV)
    df_meteo = pd.read_csv('datos_ordenados.csv')
    
    # Cargar el archivo de cuentas (formato TXT, separado por espacios)
    df_cuentas = pd.read_csv('cuentas.txt', sep=' ', header=None, names=['Fecha', 'Hora', 'Cuentas'])
except FileNotFoundError:
    print("Error: No se encontró uno de los archivos. Asegúrate de que 'presion_y_temperatura.csv' y 'cuentas.txt' estén en el mismo directorio.")
    # El script se detiene si no se encuentran los archivos.
    exit()

# --- 2. Unir las columnas de fecha y hora en un solo 'timestamp' ---
df_meteo['timestamp'] = pd.to_datetime(df_meteo['Fecha'] + ' ' + df_meteo['Hora'])
df_cuentas['timestamp'] = pd.to_datetime(df_cuentas['Fecha'] + ' ' + df_cuentas['Hora'])

# --- 3. Calcular la media y desviación estándar de las cuentas cada 5 minutos ---
# Usamos 'resample' para agrupar los datos de forma temporal.
df_cuentas_agrupado = df_cuentas.set_index('timestamp').resample('5T').agg(
    cuentas=('Cuentas', 'mean'),
    desviacionstncuentas=('Cuentas', 'std')
).reset_index()

# --- 4. Unir los datos de cuentas con los datos de meteorología ---
# 'merge' alinea los datos de ambos archivos según sus 'timestamp' comunes.
df_final = pd.merge(df_cuentas_agrupado, df_meteo, on='timestamp', how='inner').round(3)

# --- 5. Seleccionar y renombrar las columnas finales ---
# Creamos el DataFrame final con las columnas en el orden solicitado.
df_final = df_final[[
    'timestamp',
    'cuentas',
    'desviacionstncuentas',
    'Relative Pressure (hPa)',
    'Outdoor Temperature (°C)'
]]

# Renombramos las columnas para que coincidan con lo que pediste.
df_final.rename(columns={
    'timestamp': 'hora',
    'Relative Pressure (hPa)': 'presion',
    'Outdoor Temperature (°C)': 'temperatura'
}, inplace=True)

# --- 6. Generar el nuevo archivo CSV ---
output_filename = 'datos_consolidados.csv'
df_final.to_csv(output_filename, index=False)

print(f"¡Hecho! Se ha generado el archivo '{output_filename}' con los datos consolidados.")
import pandas as pd

# Leer el archivo original que ya contiene la presión y la temperatura
df = pd.read_csv('presion_y_temperatura.csv')

# Convertir la columna 'Date' a un formato de fecha y hora (datetime)
df['Date'] = pd.to_datetime(df['Date'])

# Separar la fecha y la hora en dos columnas distintas
df['Fecha'] = df['Date'].dt.date
df['Hora'] = df['Date'].dt.time

# Seleccionar las columnas que deseas en el nuevo archivo
# No necesitas renombrar las columnas, simplemente las seleccionas por su nombre
df_ordenado = df[['Fecha', 'Hora', 'Relative Pressure (hPa)', 'Outdoor Temperature (°C)']].sort_values(['Fecha', 'Hora'])

# Guardar el resultado en un nuevo archivo CSV
df_ordenado.to_csv('datos_ordenados.csv', index=False)
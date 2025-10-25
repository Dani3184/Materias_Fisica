import pandas as pd
import matplotlib.pyplot as plt

# --- PARTE 1: Cargar los datos de los archivos ---
try:
    # Lee el archivo de meteorología (CSV)
    df_meteo = pd.read_csv('datos_ordenados.csv')

    # Lee el archivo de cuentas (TXT)
    df_cuentas = pd.read_csv('datos_bolivia.txt', sep=' ', header=None, names=['Fecha', 'Hora', 'Cuentas'])
    
except FileNotFoundError:
    print("Error: No se encontró uno de los archivos. Asegúrate de que 'presion_y_temperatura.csv' y 'cuentas.txt' estén en el mismo directorio que el script.")
    exit()

# Combina las columnas de fecha y hora en un solo 'timestamp' para ambos DataFrames
df_meteo['Timestamp'] = pd.to_datetime(df_meteo['Fecha'] + ' ' + df_meteo['Hora'])
df_cuentas['Timestamp'] = pd.to_datetime(df_cuentas['Fecha'] + ' ' + df_cuentas['Hora'])


# --- PARTE 2: Generar el primer gráfico: Cuentas y Presión vs. Tiempo ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# Trazar las Cuentas en el eje Y primario (izquierdo)
color = 'tab:red'
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Cuentas', color=color)
ax1.plot(df_cuentas['Timestamp'], df_cuentas['Cuentas'], color=color, marker='o', label='Cuentas')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje Y para la Presión
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Presión (hPa)', color=color)
ax2.plot(df_meteo['Timestamp'], df_meteo['Relative Pressure (hPa)'], color=color, marker='x', label='Presión')
ax2.tick_params(axis='y', labelcolor=color)

# Configuración y visualización del gráfico
fig.suptitle('Cuentas y Presión vs. Tiempo', fontsize=16)
fig.autofmt_xdate() # Formatea las fechas del eje X para que no se superpongan
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
plt.grid(True)
plt.show()


# --- PARTE 3: Generar el segundo gráfico: Cuentas y Temperatura vs. Tiempo ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# Trazar las Cuentas en el eje Y primario
color = 'tab:red'
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Cuentas', color=color)
ax1.plot(df_cuentas['Timestamp'], df_cuentas['Cuentas'], color=color, marker='o', label='Cuentas')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje Y para la Temperatura
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Temperatura (°C)', color=color)
ax2.plot(df_meteo['Timestamp'], df_meteo['Outdoor Temperature (°C)'], color=color, marker='s', label='Temperatura')
ax2.tick_params(axis='y', labelcolor=color)

# Configuración y visualización del segundo gráfico
fig.suptitle('Cuentas y Temperatura vs. Tiempo', fontsize=16)
fig.autofmt_xdate()
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
plt.grid(True)
plt.show()
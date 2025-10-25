import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Cargar los datos del archivo consolidado ---
try:
    df = pd.read_csv('datos_consolidados.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'. Asegúrate de que esté en el mismo directorio.")
    exit()

# --- 2. Convertir la columna 'hora' a formato de fecha y hora ---
df['hora'] = pd.to_datetime(df['hora'])

# --- 3. Generar el primer gráfico: Cuentas y Presión vs. Tiempo ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# Trazar las Cuentas en el eje Y primario (izquierdo)
color = 'tab:red'
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Cuentas', color=color)
ax1.plot(df['hora'], df['cuentas'], color=color, marker='o', label='Cuentas')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje Y para la Presión
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Presión (hPa)', color=color)
ax2.plot(df['hora'], df['presion'], color=color, linestyle='--', marker='x', label='Presión')
ax2.tick_params(axis='y', labelcolor=color)

# Configuración y visualización del gráfico
fig.suptitle('Cuentas y Presión vs. Tiempo', fontsize=16)
fig.autofmt_xdate()
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
plt.grid(True)
plt.show()

# --- 4. Generar el segundo gráfico: Cuentas y Temperatura vs. Tiempo ---
fig, ax1 = plt.subplots(figsize=(12, 6))

# Trazar las Cuentas en el eje Y primario
color = 'tab:red'
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Cuentas', color=color)
ax1.plot(df['hora'], df['cuentas'], color=color, marker='o', label='Cuentas')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje Y para la Temperatura
ax2 = ax1.twinx()
color = 'tab:green'
ax2.set_ylabel('Temperatura (°C)', color=color)
ax2.plot(df['hora'], df['temperatura'], color=color, linestyle='--', marker='s', label='Temperatura')
ax2.tick_params(axis='y', labelcolor=color)

# Configuración y visualización del segundo gráfico
fig.suptitle('Cuentas y Temperatura vs. Tiempo', fontsize=16)
fig.autofmt_xdate()
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')
plt.grid(True)
plt.show()
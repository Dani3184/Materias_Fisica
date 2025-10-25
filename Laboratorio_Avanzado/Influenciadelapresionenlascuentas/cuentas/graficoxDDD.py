import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime

# Nombre del archivo de datos combinado
archivo_datos = 'datos_combinados.csv'

# Listas para almacenar los datos
fechas = []
medias = []
presiones = []

# Leer el archivo CSV
with open(archivo_datos, 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    next(lector)  # Omitir el encabezado
    
    for fila in lector:
        fechas.append(datetime.strptime(fila[0], '%Y-%m-%d %H:%M:%S'))
        medias.append(float(fila[1]))
        presiones.append(float(fila[3]))

# Crear la figura y el primer eje (para las cuentas)
fig, ax1 = plt.subplots(figsize=(12, 7))

# Crear el segundo eje que comparte el mismo eje X (para la presión)
ax2 = ax1.twinx()

# Graficar los datos
ax1.plot(fechas, medias, 'b-o', label='Media de Cuentas', markersize=5)
ax2.plot(fechas, presiones, 'r-s', label='Valor de Presión', markersize=5)

# --- INICIO de la sección mejorada para el Eje X ---

# Formatear el eje X para que solo se muestre la hora y los minutos
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Establecer la ubicación de las etiquetas del eje X cada 30 minutos
ax1.xaxis.set_major_locator(mdates.MinuteLocator(interval=60))

# Rotar las etiquetas para que no se superpongan
plt.xticks(rotation=90, ha='right')

# --- FIN de la sección mejorada para el Eje X ---

# Configurar los ejes y títulos
ax1.set_xlabel('Hora')
ax1.set_ylabel('Media de Cuentas', color='b')
ax2.set_ylabel('Valor de Presión', color='r')
ax1.set_title('Media de Cuentas vs. Presión')

# Unir las leyendas de ambos ejes en una sola
lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc='upper left')

plt.grid(True)
plt.tight_layout()
plt.savefig("Lamb davspres")
plt.show()
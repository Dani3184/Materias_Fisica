import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
from datetime import datetime

# Nombre del archivo de datos
nombre_archivo = 'estadisticas_5min.csv'

# Listas para almacenar los datos
fechas = []
medias = []
desviaciones_estandar = []

# Leer el archivo CSV
with open(nombre_archivo, 'r') as archivo_csv:
    lector = csv.reader(archivo_csv)
    # Omitir la fila de encabezado
    next(lector)
    
    for fila in lector:
        try:
            # La primera columna (Hora) es para el eje X
            # Convertimos la cadena de texto a un objeto datetime
            fechas.append(datetime.strptime(fila[0], '%Y-%m-%d %H:%M:%S'))
            # La segunda columna (Media) es el valor principal para el eje Y
            medias.append(float(fila[1]))
            # La tercera columna (Desviacion_Estandar) es para las barras de error
            desviaciones_estandar.append(float(fila[2]))
        except (ValueError, IndexError) as e:
            print(f"Error al procesar la fila: {fila}. Detalles: {e}")
            continue

# Crear la figura y los ejes de la gráfica
fig, ax = plt.subplots(figsize=(12, 7))

# Graficar los datos. 'yerr' añade las barras de error a partir de la 3ra columna.
ax.errorbar(fechas, medias, yerr=desviaciones_estandar, fmt='o-', capsize=5, label='Media con Desviación Estándar')

# --- Seccion para mejorar el eje X ---

# Usar un formateador de fechas para el eje X
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Configurar el localizador de fechas para mostrar una etiqueta cada 5 o 10 minutos
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=15))

# Rotar las etiquetas del eje X para que no se superpongan
plt.xticks(rotation=45, ha='right')

# --- Fin de la seccion de mejora ---

# Configurar el resto del diseño de la gráfica
ax.set_title('Valores de Media con Desviación Estándar', fontsize=16)
ax.set_xlabel('Hora', fontsize=12)
ax.set_ylabel('Valores de Media', fontsize=12)

# Añadir una leyenda, una cuadrícula y ajustar el diseño
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Mostrar la gráfica
plt.savefig("Cuentas.jpg")
plt.show()
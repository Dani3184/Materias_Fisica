import pandas as pd
import matplotlib.pyplot as plt

# Leer los archivos
lab = pd.read_csv('presion_ordenado.csv')
sensor1 = pd.read_csv('promedios_5min.csv')
sensor2 = pd.read_csv('promedios_5min2.csv')

# Unir fecha y hora en ambos para crear la columna datetime
lab['datetime'] = pd.to_datetime(lab['Fecha'] + ' ' + lab['Hora'])
sensor1['datetime'] = pd.to_datetime(sensor1['Fecha'] + ' ' + sensor1['Hora'])
sensor2['datetime'] = pd.to_datetime(sensor2['Fecha'] + ' ' + sensor2['Hora'])

# Ajustar la presión del sensor1 (dividir por 100 si es necesario)
sensor1['presion'] = sensor1['presion'] / 100

# Graficar
plt.figure(figsize=(14,7))
plt.plot(lab['datetime'], lab['Dato'], label='Laboratorio', color='blue')
plt.plot(sensor1['datetime'], sensor1['presion'], label='Sensor 1', color='orange')
plt.plot(sensor2['datetime'], sensor2['presion'], label='Sensor 2', color='green')
plt.xlabel('Fecha y Hora')
plt.ylabel('Presión (hPa)')
plt.title('Comparación de presión vs tiempo')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('comparacion_presion_3.png')
plt.show()
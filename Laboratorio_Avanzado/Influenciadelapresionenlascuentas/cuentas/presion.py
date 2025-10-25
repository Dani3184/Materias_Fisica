import matplotlib.pyplot as plt
from datetime import datetime

# Leer y mostrar información del archivo
fechas = []
presiones = []

with open('presion_ordenado2.csv', 'r') as f:
    print("Primeras 5 líneas del archivo:")
    for i, linea in enumerate(f):
        if i < 5:
            print(f"Línea {i}: {linea.strip()}")
        if i == 0:  # Saltar cabecera
            continue
        partes = linea.strip().split(',')
        if len(partes) == 3:
            try:
                fecha = datetime.strptime(f"{partes[0]} {partes[1]}", '%Y-%m-%d %H:%M:%S')
                presion = float(partes[2])
                fechas.append(fecha)
                presiones.append(presion)
            except Exception as e:
                print(f"Error en línea {i}: {linea.strip()} - {e}")

print(f"\nDatos leídos: {len(presiones)}")

# Graficar si hay datos
if presiones:
    plt.figure(figsize=(12, 6))
    plt.plot(fechas, presiones, 'r-o', markersize=3)
    plt.title('Presión Atmosférica vs Tiempo')
    plt.xlabel('Tiempo')
    plt.ylabel('Presión (hPa)')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("No se pudieron leer datos del archivo")
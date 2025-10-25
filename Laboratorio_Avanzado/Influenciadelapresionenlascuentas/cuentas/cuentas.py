import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# Leer los datos de cuentas
fechas = []
cuentas = []

with open('datos_bolivia.txt', 'r') as f:
    for linea in f:
        partes = linea.strip().split()
        if len(partes) >= 3:
            fecha_str = f"{partes[0]} {partes[1]}"
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
            cuenta = int(partes[2])
            fechas.append(fecha)
            cuentas.append(cuenta)

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.plot(fechas, cuentas, 'b-o', markersize=4, linewidth=1, alpha=0.7)
plt.title('Cuentas de Rayos Cósmicos vs Tiempo', fontsize=14, fontweight='bold')
plt.xlabel('Tiempo', fontsize=12)
plt.ylabel('Cuentas', fontsize=12)
plt.grid(True, alpha=0.3)

# Formatear el eje de tiempo
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Mostrar estadísticas básicas
print(f"Total de datos: {len(cuentas)}")
print(f"Cuenta máxima: {max(cuentas)}")
print(f"Cuenta mínima: {min(cuentas)}")
print(f"Cuenta promedio: {sum(cuentas)/len(cuentas):.2f}")
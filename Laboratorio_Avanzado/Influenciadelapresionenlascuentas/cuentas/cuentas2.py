from datetime import datetime, timedelta
import numpy as np

# Leer los datos originales
datos = []
with open('datos_bolivia.txt', 'r') as f:
    for linea in f:
        partes = linea.strip().split()
        if len(partes) >= 3:
            fecha_str = f"{partes[0]} {partes[1]}"
            tiempo = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M:%S')
            cuenta = int(partes[2])
            datos.append((tiempo, cuenta))

# Ordenar por tiempo (por si acaso)
datos.sort(key=lambda x: x[0])

# Agrupar por intervalos de 5 minutos
resultados = []
grupo_actual = []
tiempo_inicio = datos[0][0].replace(second=0, microsecond=0)
tiempo_actual = tiempo_inicio.replace(minute=(tiempo_inicio.minute // 5) * 5)

for tiempo, cuenta in datos:
    # Si estamos en un nuevo intervalo de 5 minutos
    if tiempo >= tiempo_actual + timedelta(minutes=5):
        if grupo_actual:
            # Calcular estadísticas del grupo anterior
            media = np.mean(grupo_actual)
            desviacion = np.std(grupo_actual)
            resultados.append((tiempo_actual, media, desviacion, len(grupo_actual)))
        
        # Reiniciar para el nuevo intervalo
        grupo_actual = []
        tiempo_actual += timedelta(minutes=5)
        
        # Saltar intervalos vacíos si es necesario
        while tiempo >= tiempo_actual + timedelta(minutes=5):
            tiempo_actual += timedelta(minutes=5)
    
    grupo_actual.append(cuenta)

# Procesar el último grupo
if grupo_actual:
    media = np.mean(grupo_actual)
    desviacion = np.std(grupo_actual)
    resultados.append((tiempo_actual, media, desviacion, len(grupo_actual)))

# Guardar resultados en archivo
with open('estadisticas_5min.csv', 'w') as f:
    f.write("Hora,Media,Desviacion_Estandar,Numero_Mediciones\n")
    for tiempo, media, desviacion, n in resultados:
        f.write(f"{tiempo.strftime('%Y-%m-%d %H:%M:%S')},{media:.2f},{desviacion:.2f},{n}\n")

print("Archivo 'estadisticas_5min.csv' generado exitosamente!")
print(f"Se procesaron {len(resultados)} intervalos de 5 minutos")

# Mostrar primeras 10 líneas como ejemplo
print("\nPrimeras 10 líneas del archivo:")
with open('estadisticas_5min.csv', 'r') as f:
    for i, linea in enumerate(f):
        if i < 11:  # Cabecera + 10 datos
            print(linea.strip())
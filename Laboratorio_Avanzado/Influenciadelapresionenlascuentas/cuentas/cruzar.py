from datetime import datetime

# Nombres de archivos
archivo_presion = "datos_ambientales_ordenados.csv"
archivo_cuentas = "estadisticas_5min.csv"
archivo_salida = "datos_combinados2.csv"

# Leer y combinar datos
with open(archivo_presion, 'r') as f1, open(archivo_cuentas, 'r') as f2, open(archivo_salida, 'w') as out:
    # Saltar cabeceras y leer datos
    next(f1)
    next(f2)
    
    # Escribir nueva cabecera
    out.write("Hora,Presion,Temperatura,Media_Cuentas,Desviacion_Cuentas,Mediciones\n")
    
    # Leer todas las líneas
    lineas_presion = f1.readlines()
    lineas_cuentas = f2.readlines()
    
    # Procesar línea por línea (asumiendo mismo orden y misma cantidad)
    for i in range(min(len(lineas_presion), len(lineas_cuentas))):
        # Procesar línea de presión
        partes_p = lineas_presion[i].strip().split(',')
        hora_p = partes_p[0].split('-04:00')[0].strip()
        presion = partes_p[1]
        temp = partes_p[2]
        
        # Procesar línea de cuentas
        partes_c = lineas_cuentas[i].strip().split(',')
        hora_c = partes_c[0].strip()
        media = partes_c[1]
        desviacion = partes_c[2]
        mediciones = partes_c[3]
        
        # Escribir línea combinada
        out.write(f"{hora_p},{presion},{temp},{media},{desviacion},{mediciones}\n")

print(f"Archivo combinado creado: {archivo_salida}")
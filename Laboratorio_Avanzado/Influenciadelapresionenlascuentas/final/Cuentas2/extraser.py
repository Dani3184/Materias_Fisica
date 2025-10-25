import csv

# Define el nombre del archivo de entrada
input_file = 'ambient-weather-20250904-20250905.csv'

# Define el nombre del nuevo archivo de salida
output_file = 'presion_y_temperatura.csv'

with open(input_file, 'r', encoding='utf-8') as csvfile_in, \
     open(output_file, 'w', newline='', encoding='utf-8') as csvfile_out:
    
    # Crea un lector que trata cada fila como un diccionario
    reader = csv.DictReader(csvfile_in)
    
    # Crea un escritor para el nuevo archivo
    writer = csv.writer(csvfile_out)
    
    # Escribe los encabezados para las columnas que quieres guardar
    writer.writerow(['Date', 'Relative Pressure (hPa)', 'Outdoor Temperature (°C)'])
    
    # Itera sobre cada fila del archivo de entrada
    for row in reader:
        # Extrae los valores de las tres columnas y escríbelos en el nuevo archivo
        writer.writerow([row['Date'], row['Relative Pressure (hPa)'], row['Outdoor Temperature (°C)']])
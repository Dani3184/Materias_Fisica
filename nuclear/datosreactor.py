import serial
import time
from datetime import datetime
import csv

# --- CONFIGURACIÓN ---
PUERTO_SERIAL = 'COM5' # <--- ¡VERIFICA Y CAMBIA ESTO!
BAUD_RATE = 9600
NOMBRE_ARCHIVO = 'registro_temperaturas_ds18b20.csv' 

# --- FUNCIÓN PRINCIPAL ---
def leer_y_guardar_datos():
    """Establece la conexión serial, lee datos T1,T2 y los guarda con timestamp."""
    
    try:
        # 1. Establecer conexión
        ser = serial.Serial(PUERTO_SERIAL, BAUD_RATE, timeout=1)
        time.sleep(2) # Espera para inicializar el puerto
        print(f"Conectado y leyendo en {PUERTO_SERIAL}. Presiona Ctrl+C para detener.")
        
        # 2. Abrir CSV y escribir encabezados (solo si el archivo es nuevo)
        with open(NOMBRE_ARCHIVO, 'a', newline='') as file:
            writer = csv.writer(file)
            # Comprueba si el archivo está vacío para escribir encabezados
            if file.tell() == 0:
                 writer.writerow(["Timestamp", "Sensor_1_C", "Sensor_2_C"])

        # 3. Bucle de lectura
        while True:
            # Lee hasta encontrar el carácter de nueva línea (\n)
            if ser.in_waiting > 0:
                linea_bytes = ser.readline()
                
                try:
                    # Decodificar, limpiar espacios y saltos de línea
                    linea_str = linea_bytes.decode('utf-8').strip()
                    
                    # Dividir la línea usando la coma como separador
                    datos = linea_str.split(',') 
                    
                    if len(datos) == 2:
                        # Convertir a float
                        temp1 = float(datos[0])
                        temp2 = float(datos[1])

                        # Registrar la hora
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        
                        # Mostrar en consola
                        print(f"[{timestamp}] T1 (Ext): {temp1:.2f} C | T2 (Olla): {temp2:.2f} C")

                        # Guardar en CSV
                        with open(NOMBRE_ARCHIVO, 'a', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow([timestamp, f"{temp1:.2f}", f"{temp2:.2f}"])
                                
                except ValueError:
                    # Ignorar si la línea no contiene dos números válidos
                    # Esto atrapa datos mal formados, líneas vacías o texto.
                    pass
                except UnicodeDecodeError:
                    # Ignorar si hay caracteres extraños en el stream
                    pass
            
            # Pausa ligera para no saturar el CPU (opcional, el Arduino ya tiene un delay)
            time.sleep(0.01) 

    except serial.SerialException as e:
        print(f"\nERROR: No se pudo conectar a {PUERTO_SERIAL}. Revisa si el puerto está abierto en el IDE de Arduino.")
    except KeyboardInterrupt:
        print("\nRegistro de temperaturas detenido por el usuario.")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("Puerto serial cerrado.")

if __name__ == "__main__":
    leer_y_guardar_datos()
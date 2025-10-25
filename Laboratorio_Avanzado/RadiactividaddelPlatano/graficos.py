import matplotlib.pyplot as plt
import numpy as np

# --- 1. Definir los archivos y sus etiquetas ---
archivos = {
    "Fondo Promediado": "fondo_promediado.txt",
    "Cesio-137 (Medición 1)": "Cs137verdader1.txt",
    "Cesio-137 (Medición 2)": "Cs137verdader2.txt",
    "Cobalto-60": "Co60verdader.txt"
}

# --- 2. Crear la figura y el eje ---
plt.figure(figsize=(10, 6)) # Define el tamaño del gráfico
plt.title("Espectros Individuales y Fondo Promediado")
plt.xlabel("Canal")
plt.ylabel("Cuentas")
plt.grid(True)

# Opcional: Escala Logarítmica en Y (común en espectros)
plt.yscale('log')

# --- 3. Leer y graficar cada archivo ---
for etiqueta, nombre_archivo in archivos.items():
    try:
        # np.loadtxt lee los datos del archivo.
        # unpack=True transpone la matriz para que X y Y sean listas separadas.
        X, Y = np.loadtxt(nombre_archivo, usecols=(0, 1), unpack=True)
        
        # Grafica los datos. El parámetro 'label' es para la leyenda.
        plt.plot(X, Y, label=etiqueta, linewidth=2)
        
    except FileNotFoundError:
        print(f"Advertencia: El archivo '{nombre_archivo}' no se encontró. Saltando...")
    except Exception as e:
        print(f"Error al procesar '{nombre_archivo}': {e}")


# --- 4. Finalizar y mostrar el gráfico ---
plt.legend(loc='upper right') # Muestra la leyenda
plt.tight_layout() # Ajusta el diseño
plt.show() # Muestra la ventana del gráfico
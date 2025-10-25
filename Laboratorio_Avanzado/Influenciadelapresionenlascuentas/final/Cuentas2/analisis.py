import pandas as pd
import matplotlib.pyplot as plt
# --- 1. Cargar el archivo consolidado ---
try:
    df = pd.read_csv('datos_consolidados.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'. Asegúrate de que esté en el mismo directorio.")
    exit()

# --- 2. Convertir cada columna a una lista (vector) ---
# La columna 'hora' se convierte a un formato de texto para mayor flexibilidad si no necesitas cálculos de tiempo.
horas = df['hora'].tolist()

# Las siguientes columnas numéricas se convierten a listas de números
cuentas = df['cuentas'].tolist()
desviacionstncuentas = df['desviacionstncuentas'].tolist()
presion = df['presion'].tolist()
temperatura = df['temperatura'].tolist()

plt.fig
plt.hist(cuentas)

# --- 3. Imprimir los vectores para verificar los datos (opcional) ---
# print("Vector de Horas:", horas)
# print("Vector de Cuentas:", cuentas)
# print("Vector de Desviación Estándar de Cuentas:", desviacionstncuentas)
# print("Vector de Presión:", presion)
# print("Vector de Temperatura:", temperatura)



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# --- 1. Cargar los datos consolidados ---
try:
    df = pd.read_csv('datos_consolidados.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'. Asegúrate de que esté en el mismo directorio.")
    exit()

# --- 2. Preparar los datos para la regresión ---
# Calcular el logaritmo natural de la columna 'cuentas'
# Añadimos un pequeño valor (1e-9) para evitar errores con log(0) si ocurriera
df['log_cuentas'] = np.log(df['cuentas'] + 1e-9)

# Variables independientes (X)
X_presion = df['presion'].values.reshape(-1, 1)
X_temperatura = df['temperatura'].values.reshape(-1, 1)

# Variable dependiente (y) es el logaritmo de las cuentas
y_log_cuentas = df['log_cuentas'].values

# --- 3. Modelo de Regresión Lineal: Log(Cuentas) vs. Presión ---
modelo_presion_log = LinearRegression()
modelo_presion_log.fit(X_presion, y_log_cuentas)

# Coeficientes
pendiente_presion = modelo_presion_log.coef_[0]
intercepto_presion = modelo_presion_log.intercept_
r2_presion = modelo_presion_log.score(X_presion, y_log_cuentas)

# --- 4. Generar el gráfico de Log(Cuentas) vs. Presión ---
plt.figure(figsize=(10, 6))

# Trazar los puntos de datos reales transformados (log_cuentas vs. presion)
plt.scatter(X_presion, y_log_cuentas, color='blue', label='Datos transformados')

# Trazar la línea de regresión
plt.plot(X_presion, modelo_presion_log.predict(X_presion), color='red', linewidth=2, label='Línea de Regresión')

# Añadir la ecuación y R^2
plt.title('Regresión Lineal: Log(Cuentas) vs. Presión', fontsize=16)
plt.xlabel('Presión (hPa)')
plt.ylabel('Log(Cuentas)')
plt.text(0.05, 0.95, f'Ecuación: y = {pendiente_presion:.6f}x + {intercepto_presion:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f'R^2 = {r2_presion:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.grid(True)
plt.savefig("RegPreson2D.jpg")
plt.show()

# --- 5. Modelo de Regresión Lineal: Log(Cuentas) vs. Temperatura ---
modelo_temperatura_log = LinearRegression()
modelo_temperatura_log.fit(X_temperatura, y_log_cuentas)

# Coeficientes
pendiente_temperatura = modelo_temperatura_log.coef_[0]
intercepto_temperatura = modelo_temperatura_log.intercept_
r2_temperatura = modelo_temperatura_log.score(X_temperatura, y_log_cuentas)

# --- 6. Generar el gráfico de Log(Cuentas) vs. Temperatura ---
plt.figure(figsize=(10, 6))

# Trazar los puntos de datos reales transformados
plt.scatter(X_temperatura, y_log_cuentas, color='blue', label='Datos transformados')

# Trazar la línea de regresión
plt.plot(X_temperatura, modelo_temperatura_log.predict(X_temperatura), color='red', linewidth=2, label='Línea de Regresión')

# Añadir la ecuación y R^2
plt.title('Regresión Lineal: Log(Cuentas) vs. Temperatura', fontsize=16)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Log(Cuentas)')
plt.text(0.05, 0.95, f'Ecuación: y = {pendiente_temperatura:.6f}x + {intercepto_temperatura:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f'R^2 = {r2_temperatura:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.grid(True)
plt.savefig("RegTemperatuda2D.jpg")
plt.show()
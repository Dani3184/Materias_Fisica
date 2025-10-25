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
# Convertir las series de pandas a arrays de numpy para scikit-learn
# El reshape(-1, 1) es necesario para que los datos tengan la forma correcta para el modelo
X_presion = df['presion'].values.reshape(-1, 1)
y_cuentas = df['cuentas'].values
X_temperatura = df['temperatura'].values.reshape(-1, 1)

# --- 3. Modelo de Regresión Lineal: Cuentas vs. Presión ---
modelo_presion = LinearRegression()
modelo_presion.fit(X_presion, y_cuentas)

# Coeficientes
pendiente_presion = modelo_presion.coef_[0]
intercepto_presion = modelo_presion.intercept_
r2_presion = modelo_presion.score(X_presion, y_cuentas)

# --- 4. Generar el gráfico de Cuentas vs. Presión ---
plt.figure(figsize=(10, 6))

# Trazar los puntos de datos reales
plt.scatter(X_presion, y_cuentas, color='blue', label='Datos reales')

# Trazar la línea de regresión (línea de mejor ajuste)
plt.plot(X_presion, modelo_presion.predict(X_presion), color='red', linewidth=2, label='Línea de Regresión')

# Añadir la ecuación y R^2 en el gráfico
plt.title('Regresión Lineal: Cuentas vs. Presión', fontsize=16)
plt.xlabel('Presión (hPa)')
plt.ylabel('Cuentas (Promedio)')
plt.text(0.05, 0.95, f'Ecuación: y = {pendiente_presion:.6f}x + {intercepto_presion:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f'R^2 = {r2_presion:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.grid(True)
plt.show()

# --- 5. Modelo de Regresión Lineal: Cuentas vs. Temperatura ---
modelo_temperatura = LinearRegression()
modelo_temperatura.fit(X_temperatura, y_cuentas)

# Coeficientes
pendiente_temperatura = modelo_temperatura.coef_[0]
intercepto_temperatura = modelo_temperatura.intercept_
r2_temperatura = modelo_temperatura.score(X_temperatura, y_cuentas)

# --- 6. Generar el gráfico de Cuentas vs. Temperatura ---
plt.figure(figsize=(10, 6))

# Trazar los puntos de datos reales
plt.scatter(X_temperatura, y_cuentas, color='blue', label='Datos reales')

# Trazar la línea de regresión (línea de mejor ajuste)
plt.plot(X_temperatura, modelo_temperatura.predict(X_temperatura), color='red', linewidth=2, label='Línea de Regresión')

# Añadir la ecuación y R^2 en el gráfico
plt.title('Regresión Lineal: Cuentas vs. Temperatura', fontsize=16)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Cuentas (Promedio)')
plt.text(0.05, 0.95, f'Ecuación: y = {pendiente_temperatura:.6f}x + {intercepto_temperatura:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f'R^2 = {r2_temperatura:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.grid(True)
plt.show()
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --- 1. Cargar el archivo consolidado ---
try:
    df = pd.read_csv('datos_consolidados.csv')
    df.columns = df.columns.str.strip() # Limpiar nombres de columnas
except FileNotFoundError:
    print("Error: The file 'datos_consolidados.csv' was not found. Make sure it's in the same directory.")
    exit()

# --- 2. Preparar y ajustar el modelo de regresión de Poisson ---
# La regresión se ajusta sobre las cuentas originales, no el log.
y = df['cuentas']
X = sm.add_constant(df[['presion', 'temperatura']])
poisson_model = sm.GLM(y, X, family=sm.families.Poisson())
poisson_res = poisson_model.fit()

# Extraer los coeficientes del modelo
intercept = poisson_res.params['const']
coef_presion = poisson_res.params['presion']
coef_temperatura = poisson_res.params['temperatura']

# --- 3. Crear el gráfico 3D ---
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

# Plotear los puntos de datos reales en la escala logarítmica
# Es importante agregar un valor pequeño (como 1e-9) para evitar log(0)
ax.scatter(df['presion'], df['temperatura'], np.log(df['cuentas'] + 1e-9), c='blue', marker='o', label='Datos reales')

# --- 4. Generar el plano de regresión ---
# Crear una cuadrícula de valores para presión y temperatura
x_surf = np.linspace(df['presion'].min(), df['presion'].max(), 100)
y_surf = np.linspace(df['temperatura'].min(), df['temperatura'].max(), 100)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

# Calcular los valores logarítmicos predichos para cada punto en la cuadrícula
# Esto representa el plano lineal del modelo
z_surf = intercept + (coef_presion * x_surf) + (coef_temperatura * y_surf)

# Plotear el plano de regresión
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.6, label='Plano de regresión Poisson')

# --- 5. Agregar etiquetas y título ---
ax.set_xlabel('Presion (hPa)')
ax.set_ylabel('Temperatura (°C)')
ax.set_zlabel('Log(Cuentas)')
ax.set_title('Plano de Regresión de Poisson', fontsize=16)

# Asegurarse de que el plano de regresión se muestre en la leyenda
# (La función plot_surface no lo añade automáticamente)
# ax.plot([], [], [], color='red', label='Plano de regresión')
# ax.legend()
plt.savefig("3DGLMpoisson_corregido.jpg")
plt.show()
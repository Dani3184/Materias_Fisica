import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression
import numpy as np

# --- 1. Cargar y preparar los datos ---
try:
    df = pd.read_csv('datos_consolidados.csv')
    df['log_cuentas'] = np.log(df['cuentas'] + 1e-9)
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'.")
    exit()

# Definir las variables
X = df[['presion', 'temperatura']].values
y = df['log_cuentas'].values

# --- 2. Ajustar el modelo de regresión lineal múltiple ---
modelo_multiple = LinearRegression()
modelo_multiple.fit(X, y)

# Coeficientes
coeficiente_presion = modelo_multiple.coef_[0]
coeficiente_temperatura = modelo_multiple.coef_[1]
intercepto = modelo_multiple.intercept_

# --- 3. Crear el gráfico 3D ---
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Trazar los puntos de datos reales
ax.scatter(df['presion'], df['temperatura'], df['log_cuentas'], c='blue', marker='o', label='Datos reales')

# Crear el plano de regresión
# Generar puntos de la cuadrícula para el plano de regresión
x_surf = np.linspace(df['presion'].min(), df['presion'].max(), 100)
y_surf = np.linspace(df['temperatura'].min(), df['temperatura'].max(), 100)
x_surf, y_surf = np.meshgrid(x_surf, y_surf)

# Calcular los valores Z (log_cuentas) para el plano usando la ecuación del modelo
z_surf = intercepto + (coeficiente_presion * x_surf) + (coeficiente_temperatura * y_surf)

# Trazar el plano de regresión
ax.plot_surface(x_surf, y_surf, z_surf, color='red', alpha=0.5, label='Plano de Regresión')

# Añadir etiquetas y título
ax.set_xlabel('Presión (hPa)')
ax.set_ylabel('Temperatura (°C)')
ax.set_zlabel('Log(Cuentas)')
ax.set_title('Regresión Lineal Múltiple en 3D', fontsize=16)
print(f"Ecuación exponencial: cuentas = exp({intercepto:.6f} "
      f"+ {coeficiente_presion:.6f} * presion "
      f"+ {coeficiente_temperatura:.6f} * temperatura)")
plt.savefig("3DregresionminimosCc.jpg")
plt.show()
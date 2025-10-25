import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

# --- 1. Cargar los datos consolidados ---
try:
    df = pd.read_csv('datos_consolidados.csv')
    df.columns = df.columns.str.strip() # Limpiar nombres de columnas
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'. Asegúrate de que esté en el mismo directorio.")
    exit()

# --- 2. Preparar los datos y ajustar el modelo Poisson ---
# La variable dependiente (y) son las cuentas originales
y = df['cuentas']

# --- 3. Modelo GLM de Poisson: Cuentas vs. Presión ---
X_presion = sm.add_constant(df['presion'])
modelo_presion_poisson = sm.GLM(y, X_presion, family=sm.families.Poisson()).fit()

# Coeficientes
pendiente_presion_poisson = modelo_presion_poisson.params['presion']
intercepto_presion_poisson = modelo_presion_poisson.params['const']

# La "correlación" en los GLMs no es R^2. Se usa la devianza o el AIC.
# Para este gráfico, mostraremos la devianza (una medida de qué tan bien se ajusta el modelo)
devianza_presion = modelo_presion_poisson.deviance

# --- 4. Generar el gráfico de Log(Cuentas) vs. Presión ---
plt.figure(figsize=(10, 6))

# Trazar los puntos de datos reales transformados (log_cuentas vs. presion)
plt.scatter(df['presion'], np.log(y + 1e-9), color='blue', label='Datos log-transformados')

# Trazar la línea de regresión de Poisson en la escala logarítmica
x_pred = np.linspace(df['presion'].min(), df['presion'].max(), 100)
# La ecuación en la escala logarítmica es: log(lambda) = intercepto + pendiente * x
y_pred_log = intercepto_presion_poisson + pendiente_presion_poisson * x_pred
plt.plot(x_pred, y_pred_log, color='red', linewidth=2, label='Regresión Poisson (plano log-lineal)')

# Añadir la ecuación y la devianza
plt.title('Regresión GLM de Poisson: Log(Cuentas) vs. Presión', fontsize=16)
plt.xlabel('Presión (hPa)')
plt.ylabel('Log(Cuentas)')
plt.text(0.05, 0.95, f'Ecuación: Log(Cuentas) = {pendiente_presion_poisson:.6f}x + {intercepto_presion_poisson:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f'Devianza: {devianza_presion:.2f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.grid(True)
plt.savefig("PressGLM2D.jpg")
plt.show()

# --- 5. Modelo GLM de Poisson: Cuentas vs. Temperatura ---
X_temperatura = sm.add_constant(df['temperatura'])
modelo_temperatura_poisson = sm.GLM(y, X_temperatura, family=sm.families.Poisson()).fit()

# Coeficientes
pendiente_temperatura_poisson = modelo_temperatura_poisson.params['temperatura']
intercepto_temperatura_poisson = modelo_temperatura_poisson.params['const']
devianza_temperatura = modelo_temperatura_poisson.deviance

# --- 6. Generar el gráfico de Log(Cuentas) vs. Temperatura ---
plt.figure(figsize=(10, 6))

# Trazar los puntos de datos reales transformados
plt.scatter(df['temperatura'], np.log(y + 1e-9), color='blue', label='Datos log-transformados')

# Trazar la línea de regresión de Poisson en la escala logarítmica
x_pred = np.linspace(df['temperatura'].min(), df['temperatura'].max(), 100)
y_pred_log = intercepto_temperatura_poisson + pendiente_temperatura_poisson * x_pred
plt.plot(x_pred, y_pred_log, color='red', linewidth=2, label='Regresión Poisson (plano log-lineal)')

# Añadir la ecuación y la devianza
plt.title('Regresión GLM de Poisson: Log(Cuentas) vs. Temperatura', fontsize=16)
plt.xlabel('Temperatura (°C)')
plt.ylabel('Log(Cuentas)')
plt.text(0.05, 0.95, f'Ecuación: Log(Cuentas) = {pendiente_temperatura_poisson:.6f}x + {intercepto_temperatura_poisson:.6f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.text(0.05, 0.90, f'Devianza: {devianza_temperatura:.2f}',
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
plt.legend()
plt.grid(True)
plt.savefig("Temp2DGLM.jpg")
plt.show()
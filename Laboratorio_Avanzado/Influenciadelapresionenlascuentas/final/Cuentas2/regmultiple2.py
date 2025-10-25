import pandas as pd
import numpy as np
import statsmodels.api as sm

# --- 1. Cargar y preparar los datos ---
try:
    df = pd.read_csv('datos_consolidados.csv')
    df.columns = df.columns.str.strip()  # Limpiar nombres de columnas
    # Transformar la variable dependiente a escala logarítmica
    df['log_cuentas'] = np.log(df['cuentas'] + 1e-9)
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'.")
    exit()

# --- 2. Preparar variables para el modelo OLS (Mínimos Cuadrados) ---
# Y es la variable dependiente (log(cuentas))
y = df['log_cuentas']
# X son las variables independientes (presión y temperatura), incluyendo el intercepto
X = sm.add_constant(df[['presion', 'temperatura']])

# --- 3. Ajustar el modelo de regresión lineal (OLS) ---
modelo_ols = sm.OLS(y, X)
resultados_ols = modelo_ols.fit()

# --- 4. Imprimir el resumen estadístico completo ---
print("\n=== Resumen del Modelo de Regresión Lineal (OLS) ===")
print(resultados_ols.summary())

# --- 5. Extraer y mostrar los parámetros principales ---
print("\n=== Coeficientes y P-valores ===")
print(resultados_ols.params)
print("\n=== P-valores ===")
print(resultados_ols.pvalues)
print("\n=== Intervalos de Confianza (95%) ===")
print(resultados_ols.conf_int(alpha=0.05))
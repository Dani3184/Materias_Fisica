import pandas as pd
import statsmodels.api as sm
import numpy as np

# === 1. Leer datos ===
data = pd.read_csv("datos_combinados2.csv")

# Variables independientes
X = data[["Presion", "Temperatura"]]

# === 2a. Regresión Lineal (sobre log de las cuentas) ===
y_log = np.log(data["Media_Cuentas"])
X_lin = sm.add_constant(X)  # añade intercepto
modelo_lin = sm.OLS(y_log, X_lin).fit()
print("=== Regresión Lineal (log) ===")
print(modelo_lin.summary())

# === 2b. Regresión de Poisson ===
y = data["Media_Cuentas"].astype(int)  # cuentas
X_pois = sm.add_constant(X)
modelo_pois = sm.GLM(y, X_pois, family=sm.families.Poisson()).fit()
print("\n=== Regresión de Poisson ===")
print(modelo_pois.summary())

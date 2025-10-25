import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# === 1. Leer datos ===
df = pd.read_csv("datos_combinados2.csv", parse_dates=["Hora"])

# === 2. Definir umbrales ===
umbral_min = 200
umbral_max = 1000

# Filtrar datos dentro del rango de cuentas
df = df[(df["Media_Cuentas"] >= umbral_min) & (df["Media_Cuentas"] <= umbral_max)]

# Eliminar posibles ceros para el logaritmo
df = df[df["Media_Cuentas"] > 0]

print(f"Datos restantes: {len(df)} en el rango [{umbral_min}, {umbral_max}]")

# === 3. Regresión Lineal (sobre log) ===
df["log_Cuentas"] = np.log(df["Media_Cuentas"])

modelo_lineal = smf.ols("log_Cuentas ~ Presion + Temperatura", data=df).fit()
print("\n📌 Regresión Lineal (log):")
print(modelo_lineal.summary())

# === 4. Regresión de Poisson (GLM) ===
modelo_poisson = smf.glm("Media_Cuentas ~ Presion + Temperatura",
                         data=df,
                         family=sm.families.Poisson()).fit()
print("\n📌 Regresión de Poisson (GLM):")
print(modelo_poisson.summary())


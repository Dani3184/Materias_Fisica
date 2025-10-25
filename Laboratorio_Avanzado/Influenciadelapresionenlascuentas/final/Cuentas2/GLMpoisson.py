import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy import stats

# --- 1. Cargar el archivo consolidado ---
try:
    df = pd.read_csv('datos_consolidados.csv')
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'. Asegúrate de que esté en el mismo directorio.")
    exit()

# --- 2. Preparar variables ---
# X = variables independientes (con intercepto)
X = sm.add_constant(df[['presion', 'temperatura']])

# y = variable dependiente (cuentas, se recomienda usar totales, no promedios)
y = df['cuentas']

# --- 3. Ajustar modelo Poisson ---
poisson_model = sm.GLM(y, X, family=sm.families.Poisson())
poisson_res = poisson_model.fit()
print("\n=== Modelo Poisson ===")
print(poisson_res.summary())

# --- 4. Extraer resultados (coef, p-valores, IC) ---
coefs = poisson_res.params
ses = poisson_res.bse
z_vals = coefs / ses
p_vals = 2 * stats.norm.sf(np.abs(z_vals))   # p-valores bilaterales

result_table = pd.DataFrame({
    'coef': coefs,
    'std_err': ses,
    'z': z_vals,
    'p_value': p_vals,
    '95% CI low': poisson_res.conf_int()[0],
    '95% CI high': poisson_res.conf_int()[1]
})
print("\n=== Coeficientes y p-valores (Poisson) ===")
print(result_table)

# --- 5. Interpretación multiplicativa (Rate Ratios) ---
rr = np.exp(coefs)
ci_lower = np.exp(poisson_res.conf_int()[0])
ci_upper = np.exp(poisson_res.conf_int()[1])

rr_table = pd.DataFrame({
    'rate_ratio': rr,
    'RR 95% low': ci_lower,
    'RR 95% high': ci_upper
})
print("\n=== Rate Ratios (interpretación multiplicativa) ===")
print(rr_table)

# --- 6. Chequeo de sobredispersión ---
pearson_chi2 = sum(poisson_res.resid_pearson**2)
dispersion = pearson_chi2 / poisson_res.df_resid
print("\n=== Chequeo de sobredispersión ===")
print(f"Pearson Chi2 = {pearson_chi2:.2f}")
print(f"Grados de libertad = {poisson_res.df_resid}")
print(f"Dispersion = {dispersion:.2f}")
if dispersion > 2:
    print("⚠️ Hay sobredispersión significativa: considerar modelo Negativo Binomial.")
else:
    print("No se observa sobredispersión importante.")

# --- 7. Modelo Negativo Binomial (para comparar si hay sobredispersión) ---
nb_model = sm.GLM(y, X, family=sm.families.NegativeBinomial())
nb_res = nb_model.fit()
print("\n=== Modelo Negativo Binomial ===")
print(nb_res.summary())

# Comparar AIC
print("\n=== Comparación AIC ===")
print(f"AIC Poisson: {poisson_res.aic:.2f}")
print(f"AIC NB     : {nb_res.aic:.2f}")

# --- 8. Guardar resultados en CSV ---
result_table.to_csv("coeficientes_poisson.csv", index=True)
rr_table.to_csv("rate_ratios_poisson.csv", index=True)

print("\n✅ Tablas guardadas: coeficientes_poisson.csv, rate_ratios_poisson.csv")

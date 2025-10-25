import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# --- 1. Definir el intervalo de tiempo para calcular la media ---
# Puedes cambiar este valor según lo que necesites
# '30T' = 30 minutos
# '15T' = 15 minutos
# 'H' = 1 hora
intervalo_de_media = 'H'

# --- 2. Cargar el archivo y preparar los datos ---
try:
    df = pd.read_csv('datos_consolidados.csv')
    df.columns = df.columns.str.strip()
    df['hora'] = pd.to_datetime(df['hora'])
except FileNotFoundError:
    print("Error: No se encontró el archivo 'datos_consolidados.csv'.")
    exit()

# --- 3. Calcular las medias según el intervalo y unirlas al DataFrame original ---
# Crear una columna con el 'piso' del intervalo de tiempo
df['intervalo_tiempo'] = df['hora'].dt.floor(intervalo_de_media)

# Calcular la media de presión y temperatura para cada intervalo
medias_intervalo = df.groupby('intervalo_tiempo')[['presion', 'temperatura']].mean().reset_index()
medias_intervalo.columns = ['intervalo_tiempo', 'media_presion', 'media_temperatura']

# Unir las medias al DataFrame original
df = pd.merge(df, medias_intervalo, on='intervalo_tiempo')

# --- 4. Calcular las variables de diferencia (Delta) ---
df['delta_P'] = df['presion'] - df['media_presion']
df['delta_T'] = df['temperatura'] - df['media_temperatura']

# --- 5. Ajustar un único Modelo Lineal Generalizado (GLM) de Poisson ---
X = sm.add_constant(df[['delta_P', 'delta_T']])
y = df['cuentas']
modelo_glm = sm.GLM(y, X, family=sm.families.Poisson())
resultados_glm = modelo_glm.fit()

# Extraer los coeficientes del modelo
intercepto = resultados_glm.params['const']
coef_delta_P = resultados_glm.params['delta_P']
coef_delta_T = resultados_glm.params['delta_T']

print(f"--- Modelo GLM de Poisson (Intervalo de media: {intervalo_de_media}) ---")
print(resultados_glm.summary())

# --- 6. Generar los gráficos ---
fig, (ax_p, ax_t) = plt.subplots(1, 2, figsize=(18, 8))

# Gráfico 1: Log(Cuentas) vs. Diferencia de Presión (ΔP)
ax_p.scatter(df['delta_P'], np.log(df['cuentas'] + 1e-9), color='blue', alpha=0.5, label='Todos los datos')
x_pred_p = np.linspace(df['delta_P'].min(), df['delta_P'].max(), 100)
y_pred_p = np.exp(intercepto + coef_delta_P * x_pred_p)
ax_p.plot(x_pred_p, np.log(y_pred_p), color='red', linewidth=2, label='Línea de regresión Poisson')
ax_p.set_title(f'Log(Cuentas) vs. ΔP (Media: {intervalo_de_media})', fontsize=16)
ax_p.set_xlabel('Diferencia de Presión respecto a la media', fontsize=12)
ax_p.set_ylabel('Logaritmo de las Cuentas', fontsize=12)
ax_p.legend()
ax_p.grid(True)

# Gráfico 2: Log(Cuentas) vs. Diferencia de Temperatura (ΔT)
ax_t.scatter(df['delta_T'], np.log(df['cuentas'] + 1e-9), color='blue', alpha=0.5, label='Todos los datos')
x_pred_t = np.linspace(df['delta_T'].min(), df['delta_T'].max(), 100)
y_pred_t = np.exp(intercepto + coef_delta_T * x_pred_t)
ax_t.plot(x_pred_t, np.log(y_pred_t), color='red', linewidth=2, label='Línea de regresión Poisson')
ax_t.set_title(f'Log(Cuentas) vs. ΔT (Media: {intervalo_de_media})', fontsize=16)
ax_t.set_xlabel('Diferencia de Temperatura respecto a la media', fontsize=12)
ax_t.set_ylabel('Logaritmo de las Cuentas', fontsize=12)
ax_t.legend()
ax_t.grid(True)

plt.tight_layout()
plt.savefig("DifPresTempGLM2.jpg")
plt.show()
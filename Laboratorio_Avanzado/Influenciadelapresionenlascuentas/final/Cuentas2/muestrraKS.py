import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# --- Cargar los datos ---
# El archivo tiene formato: fecha hora valor
# Necesitamos combinar las primeras dos columnas como timestamp y la tercera como cuentas
df = pd.read_csv("cuentas.txt", sep=' ', header=None, 
                 names=['fecha', 'hora', 'cuentas'])

# Combinar fecha y hora en una sola columna de timestamp
df['timestamp'] = pd.to_datetime(df['fecha'] + ' ' + df['hora'])

print("Primeras filas de datos crudos:")
print(df[['timestamp', 'cuentas']].head())
print(f"\nTotal de mediciones: {len(df)}")

# --- Seleccionar el intervalo de tiempo (11:25:00 - 11:30:00) ---
datos_intervalo = df[(df['timestamp'] >= '2025-09-04 20:00:00') & 
                     (df['timestamp'] < '2025-09-04 20:05:00')]['cuentas'].values

print(f"\nDatos del intervalo 12:00-12:05:")
print(datos_intervalo)
print(f"Número de mediciones en el intervalo: {len(datos_intervalo)}")

# --- Realizar la Prueba de Kolmogorov-Smirnov ---
lambda_estimado = np.mean(datos_intervalo)
statistic, p_value = stats.kstest(datos_intervalo, 
                                 lambda x: stats.poisson.cdf(x, mu=lambda_estimado))

print(f"\n--- Resultados de la prueba K-S ---")
print(f"Lambda estimado (media): {lambda_estimado:.2f}")
print(f"Varianza: {np.var(datos_intervalo):.2f}")
print(f"Ratio varianza/media: {np.var(datos_intervalo)/lambda_estimado:.3f}")
print(f"Estadístico D (distancia máxima): {statistic:.4f}")
print(f"Valor p: {p_value:.4f}")

# Interpretación
alpha = 0.05
if p_value > alpha:
    print("No se rechaza H₀: Los datos siguen una distribución de Poisson")
else:
    print("Se rechaza H₀: Los datos NO siguen una distribución de Poisson")

# --- Preparar los datos para la visualización ---
datos_ordenados = np.sort(datos_intervalo)
n = len(datos_ordenados)
ecdf_y = np.arange(1, n + 1) / n
cdf_teorica_y = stats.poisson.cdf(datos_ordenados, mu=lambda_estimado)

# --- Crear el gráfico ---
plt.figure(figsize=(14, 6))

# Primer subgráfico: Histograma de los datos
plt.subplot(1, 2, 1)
plt.hist(datos_intervalo, bins=range(int(min(datos_intervalo)), int(max(datos_intervalo)) + 2), 
         edgecolor='black', alpha=0.7, rwidth=0.8, density=True)
plt.title('Histograma - Datos del intervalo 20:00-20:05', fontsize=12)
plt.xlabel('Cuentas')
plt.ylabel('Densidad')
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Superponer la distribución Poisson teórica
x_vals = np.arange(int(min(datos_intervalo)), int(max(datos_intervalo)) + 1)
poisson_probs = stats.poisson.pmf(x_vals, mu=lambda_estimado)
plt.plot(x_vals, poisson_probs, 'ro-', label=f'Poisson (λ={lambda_estimado:.1f})')
plt.legend()

# Segundo subgráfico: ECDF vs. CDF
plt.subplot(1, 2, 2)
plt.step(datos_ordenados, ecdf_y, where='post', color='blue', 
         linestyle='-', marker='o', markersize=4, label='ECDF (Empírica)')
plt.plot(datos_ordenados, cdf_teorica_y, color='red', linestyle='-', 
         marker='x', markersize=4, label=f'CDF Poisson (λ={lambda_estimado:.1f})')

# Resaltar la distancia máxima (estadístico D)
max_diff = np.max(np.abs(ecdf_y - cdf_teorica_y))
diff_indices = np.where(np.abs(ecdf_y - cdf_teorica_y) == max_diff)
idx = diff_indices[0][0]

plt.plot([datos_ordenados[idx], datos_ordenados[idx]], 
         [cdf_teorica_y[idx], ecdf_y[idx]], color='green', 
         linestyle='--', linewidth=2, label=f'D = {max_diff:.3f}')
plt.text(datos_ordenados[idx], (ecdf_y[idx] + cdf_teorica_y[idx]) / 2, 
         f'D={max_diff:.3f}', color='green', fontsize=10)

plt.title('Prueba K-S: ECDF vs. CDF de Poisson', fontsize=12)
plt.xlabel('Cuentas')
plt.ylabel('Probabilidad Acumulada')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
# plt.savefig("KS1.jpg")
# plt.savefig("KS2.jpg")
plt.savefig("KS3.jpg")
plt.show()

# --- Análisis adicional ---
print(f"\n--- Estadísticas descriptivas ---")
print(f"Mínimo: {np.min(datos_intervalo)}")
print(f"Máximo: {np.max(datos_intervalo)}")
print(f"Mediana: {np.median(datos_intervalo):.1f}")
# print(f"Moda: {stats.mode(datos_intervalo)[0][0]}")

# Test de dispersión para Poisson
if len(datos_intervalo) > 1:
    try:
        dispersion_test = stats.poisson.dispersion_test(datos_intervalo)
        print(f"\nTest de dispersión - p-value: {dispersion_test.pvalue:.4f}")
    except:
        print("\nNo se pudo realizar el test de dispersión")
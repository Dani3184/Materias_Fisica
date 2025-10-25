import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, kstest

# === 1. Leer datos ===
df = pd.read_csv("estadisticas_5min.csv")

# === 2. Definir umbrales ===
umbral_min = 200
umbral_max = 1000

# Filtrar datos dentro del rango
datos = df["Media"]
datos = datos[(datos >= umbral_min) & (datos <= umbral_max)].astype(int)
n = len(datos)

if n == 0:
    print("⚠️ No hay datos en el rango especificado.")
else:
    # === 3. Estimar lambda ===
    lambda_est = np.mean(datos)
    print(f"Lambda estimado: {lambda_est:.2f} con {n} datos en el rango [{umbral_min}, {umbral_max}]")

    # === 4. Prueba KS ===
    D, p_val_ks = kstest(datos, "poisson", args=(lambda_est,))
    print(f"KS test: D={D:.3f}, p-valor={p_val_ks:.4f}")

    # === 5. Gráfico ===
    plt.figure(figsize=(10,6))
    # Histograma de datos normalizado
    plt.hist(datos, bins=30, density=True, alpha=0.6, color="skyblue", edgecolor="black", label="Datos")
    # Distribución Poisson ajustada
    x_vals = np.arange(min(datos), max(datos)+1)
    pmf_vals = poisson.pmf(x_vals, lambda_est)
    plt.plot(x_vals, pmf_vals, "r--", linewidth=2, label=f"Poisson(λ={lambda_est:.1f})")

    # Mostrar resultados en la gráfica
    plt.text(0.02, 0.95, f"KS test:\nD={D:.3f}, p={p_val_ks:.4f}",
             transform=plt.gca().transAxes, fontsize=12,
             verticalalignment="top", bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.7))

    plt.xlabel("Cuentas")
    plt.ylabel("Frecuencia relativa")
    plt.title(f"Prueba KS para datos vs Poisson\n(umbrales: {umbral_min} – {umbral_max})")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.savefig("priuebaKS1.jpg")
    plt.show()

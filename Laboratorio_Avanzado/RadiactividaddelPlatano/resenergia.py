import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# --- Datos experimentales ---
E = np.array([662, 1173.2, 1332.5, 302.85, 356, 511, 1274])
R = np.array([7.443, 6.4775, 5.79, 15.36, 11.39, 8.342, 5.654])

# --- Modelo: R(E) = a + b / sqrt(E) ---
def modelo(E, a, b):
    return a + b / np.sqrt(E)

# --- Ajuste ---
popt, pcov = curve_fit(modelo, E, R, p0=[2, 100])
a, b = popt
da, db = np.sqrt(np.diag(pcov))

print(f"Parámetros del ajuste:")
print(f"a = {a:.4f} ± {da:.4f}")
print(f"b = {b:.4f} ± {db:.4f}")

# --- Valores ajustados y residuos ---
R_fit = modelo(E, a, b)
residuos = R - R_fit

# --- Gráfico 1: Ajuste ---
plt.figure(figsize=(8,6))
plt.scatter(E, R, color="#0072BD", label="Datos experimentales", s=60)
E_fit = np.linspace(min(E)*0.9, max(E)*1.05, 300)
plt.plot(E_fit, modelo(E_fit, a, b), color="#D95319", lw=2,
         label=f"Ajuste: R(E) = {a:.2f} + {b:.1f}/√E")
plt.xlabel("Energía del fotón γ (keV)")
plt.ylabel("Resolución en Energía (%)")
plt.title("Ajuste de la Resolución en Energía del Detector NaI(Tl)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("ajuste_resolucion.png", dpi=300)
plt.close()

# --- Gráfico 2: Residuos ---
plt.figure(figsize=(8,4))
plt.scatter(E, residuos, color="#4DBEEE", s=60)
plt.axhline(0, color="black", lw=1)
plt.xlabel("Energía del fotón γ (keV)")
plt.ylabel("Residuo (%)")
plt.title("Residuos del Ajuste")
plt.grid(True)
plt.tight_layout()
plt.savefig("residuos_ajuste.png", dpi=300)
plt.close()

print("Gráficos guardados: 'ajuste_resolucion.png' y 'residuos_ajuste.png'")

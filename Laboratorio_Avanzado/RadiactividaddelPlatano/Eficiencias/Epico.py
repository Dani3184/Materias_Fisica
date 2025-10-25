import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Tus datos: [ln(ε), ln(E)]
datos = np.array([
    [-2.3497, 5.713],    # Ba-133 @ 302.85 keV
    [-2.59186, 5.875],   # Ba-133 @ 356.0 keV  
    [-2.68035, 6.236],   # Na-22 @ 511.0 keV
    [-3.5526, 7.15]      # Na-22 @ 1274.5 keV
])

# Separar variables
x = datos[:, 1]  # ln(E)
y = datos[:, 0]  # ln(ε)

# Regresión lineal
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)

print("=" * 50)
print("REGRESIÓN LINEAL - EFICIENCIA vs ENERGÍA")
print("=" * 50)
print(f"Ecuación: ln(ε) = {intercept:.4f} + {slope:.4f} × ln(E)")
print(f"Coeficiente de correlación (r): {r_value:.6f}")
print(f"R-cuadrado (r²): {r_value**2:.6f}")
print(f"Error estándar: {std_err:.6f}")
print("=" * 50)

# Calcular valores ajustados
y_pred = intercept + slope * x

# Calcular ε para 1461 keV
E_plátano = 1461
ln_E_plátano = np.log(E_plátano)
ln_ε_plátano = intercept + slope * ln_E_plátano
ε_plátano = np.exp(ln_ε_plátano)

print(f"\nEFICIENCIA PARA K-40 (1461 keV):")
print(f"ln(1461) = {ln_E_plátano:.4f}")
print(f"ln(ε) = {intercept:.4f} + {slope:.4f} × {ln_E_plátano:.4f} = {ln_ε_plátano:.4f}")
print(f"ε = exp({ln_ε_plátano:.4f}) = {ε_plátano:.6f} ({ε_plátano*100:.2f}%)")
print("=" * 50)

# Gráfico
plt.figure(figsize=(10, 6))

# Puntos experimentales
plt.scatter(x, y, color='red', s=80, label='Datos experimentales', zorder=5)

# Línea de regresión
x_fit = np.linspace(min(x)-0.2, max(x)+0.2, 100)
y_fit = intercept + slope * x_fit
plt.plot(x_fit, y_fit, 'b-', label=f'Regresión: ln(ε) = {intercept:.3f} {slope:+.3f}×ln(E)', linewidth=2)

# Punto del plátano
plt.scatter(ln_E_plátano, ln_ε_plátano, color='green', s=100, label=f'K-40 @ 1461 keV', zorder=6)

plt.xlabel('ln(Energía) [ln(keV)]', fontsize=12)
plt.ylabel('ln(Eficiencia)', fontsize=12)
plt.title('Calibración de Eficiencia del Detector Gamma', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()

# Añadir anotaciones con las energías reales
energías = [302.85, 356.0, 511.0, 1274.5]
for i, (xi, yi, E) in enumerate(zip(x, y, energías)):
    plt.annotate(f'{E} keV', (xi, yi), xytext=(5, 5), textcoords='offset points', 
                 fontsize=9, alpha=0.7)

plt.tight_layout()
plt.savefig("Epico.png")
plt.show()

# Tabla de resultados
print(f"\nTABLA DE RESULTADOS:")
print("Energía (keV) | ln(E)  | ln(ε)_exp | ln(ε)_ajust | ε_ajustada")
print("-" * 65)
for i, E in enumerate(energías):
    ln_ε_ajust = intercept + slope * x[i]
    ε_ajust = np.exp(ln_ε_ajust)
    print(f"{E:10.1f} | {x[i]:6.3f} | {y[i]:9.4f} | {ln_ε_ajust:9.4f} | {ε_ajust:8.4f}")

print(f"{1461:10.1f} | {ln_E_plátano:6.3f} | {'-':9} | {ln_ε_plátano:9.4f} | {ε_plátano:8.4f}")

# Calcular residuos
residuos = y - y_pred
print(f"\nANÁLISIS DE RESIDUOS:")
print(f"Residuos: {residuos}")
print(f"Suma de residuos: {np.sum(residuos):.6f}")
print(f"Desviación estándar de residuos: {np.std(residuos):.6f}")
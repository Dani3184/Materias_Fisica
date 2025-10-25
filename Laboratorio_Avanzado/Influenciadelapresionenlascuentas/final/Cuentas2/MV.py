import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import norm

# Cargar tus datos
df = pd.read_csv("datos_consolidados.csv")
y = df["cuentas"].values
X = np.column_stack((np.ones(len(df)), df["presion"], df["temperatura"]))

# --- Definir log-verosimilitud negativa (para minimizar) ---
def neg_loglike(params, X, y):
    linear = X @ params
    lambdas = np.exp(linear)
    # Usar la aproximación de Stirling para evitar overflow con factoriales grandes
    log_likelihood = np.sum(y * linear - lambdas - y * np.log(y + 1e-10) + y)
    return -log_likelihood

# Versión alternativa más eficiente (omite el término constante que no afecta la optimización)
def neg_loglike_simple(params, X, y):
    linear = X @ params
    lambdas = np.exp(linear)
    # Solo los términos que dependen de los parámetros
    return -np.sum(y * linear - lambdas)

# --- Estimar parámetros por MLE ---
init = np.zeros(X.shape[1])  # valores iniciales
res = minimize(neg_loglike_simple, init, args=(X, y), method="BFGS")

print("Coeficientes (MLE):", res.x)
print("Log-verosimilitud en el óptimo:", -res.fun)

# Para obtener la matriz de varianzas-covarianzas, necesitamos el hessiano
# Calculamos la matriz de información de Fisher
def hessian_poisson(params, X, y):
    linear = X @ params
    lambdas = np.exp(linear)
    W = np.diag(lambdas)
    return X.T @ W @ X

# Matriz de varianzas-covarianzas es la inversa de la matriz de información de Fisher
fisher_info = hessian_poisson(res.x, X, y)
cov_matrix = np.linalg.inv(fisher_info)

print("Matriz de varianzas-covarianzas:")
print(cov_matrix)

# Errores estándar de los coeficientes
std_errors = np.sqrt(np.diag(cov_matrix))
print("Errores estándar:", std_errors)

# Valores z y p-valores
z_scores = res.x / std_errors
p_values = 2 * (1 - norm.cdf(np.abs(z_scores)))

print("Z-scores:", z_scores)
print("P-values:", p_values)
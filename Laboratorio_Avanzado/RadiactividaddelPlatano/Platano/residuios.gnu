# ------------------------------------------------------------------
# CONFIGURACIÓN DE AJUSTE Y DATOS
# ------------------------------------------------------------------

datafile = "regresion.txt"

# 1. Definir el modelo lineal: y = m*x + b
f(x) = m*x + b

# 2. Realizar el ajuste (FIT)
# Usando 'via' para definir las variables que se van a ajustar (m y b)
fit f(x) datafile using 1:2 via m, b

# 3. Calcular el R-cuadrado (R^2)
# a) Calcular la suma total de cuadrados (SST)
stats datafile using 2 nooutput
SST = STATS_ssd

# b) Calcular la suma de cuadrados de los residuos (SSE)
stats datafile using 1:($2 - f($1)) nooutput
SSE = STATS_ssd

# c) Calcular el R^2
R_sq = 1.0 - SSE/SST
print sprintf("Coeficiente de Determinación (R^2): %.4f", R_sq)
# ------------------------------------------------------------------
# GRÁFICO 1: Regresión Lineal y Ecuación
# ------------------------------------------------------------------

set terminal wxt size 800, 600 title "Regresión Lineal y Residuos"
set multiplot layout 2, 1 title "Análisis de Regresión"

# --- Subgráfico Superior: Regresión ---
set title "Regresión Lineal: Net Counts vs. Channel"
set ylabel "Net Counts (Y)"
set xlabel "Channel (X)"
set format y "%.0f"
set key bottom right

plot datafile using 1:2 title "Datos Medidos" with points pointtype 7, \
     f(x) title sprintf("y = %.4f x + %.4f (R²=%.4f)", m, b, R_sq) with lines linewidth 2

# ------------------------------------------------------------------
# GRÁFICO 2: Análisis de Residuos
# ------------------------------------------------------------------

# --- Subgráfico Inferior: Residuos ---
set title "Análisis de Residuos"
set ylabel "Residuo (Y_{datos} - Y_{ajuste})"
unset xlabel # Usa el mismo eje X que el gráfico superior
set key off
set zeroaxis linewidth 1.5 lc "black" # Dibuja la línea horizontal Y=0

# Graficar los residuos: X (columna 1) vs. Y_residual ($2 - f($1))
plot datafile using 1:($2 - f($1)) title "Residuos" with points pointtype 5 lc "red"

unset multiplot
# ------------------------------------------------------------------
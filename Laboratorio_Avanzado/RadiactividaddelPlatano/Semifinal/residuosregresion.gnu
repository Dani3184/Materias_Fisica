reset
set fit quiet
set terminal pngcairo size 1000,600 enhanced font "Arial,12"
set output "residuos_regresion.png"

# ============================
# CONFIGURACIÓN GENERAL
# ============================
datafile = "regresionverdadera.txt"   # ← tu archivo con datos: canal (x) y energía (y)
set title "Análisis de Residuos de la Segunda Regresión"
set xlabel "Canal"
set ylabel "Residuo (Energía observada - ajustada) [keV]"
set grid

# ============================
# Parámetros de la segunda regresión
# ============================
a2 = 1.489484595
b2 = 0.7128550727
f2(x) = b2*x + a2

# ============================
# Calcular los residuos
# ============================
# '($2 - f2($1))' calcula el residuo directamente: valor observado menos valor ajustado
# Puedes graficarlos directamente o guardarlos con 'set table'
set style line 1 lc rgb "#0072BD" pt 7 ps 1.5

plot datafile using 1:($2 - f2($1)) with points ls 1 title "Residuos", \
     0 with lines lw 2 lc rgb "black" title "Residuo = 0"

unset output
set terminal wxt

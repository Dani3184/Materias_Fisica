# --- 1. Definir funciones y variables iniciales ---
m = 1; b = 0
m2 = 1; b2 = 0
f(x) = m*x + b
g(x) = m2*x + b2

R1 = 0.0 
R2 = 0.0

set pointsize 1.2

# --- 2. Archivos de datos ---
datafile1 = "regresion.txt"
datafile2 = "regresionverdadera.txt"

# --- 3. Ajustes ---
fit f(x) datafile1 using 1:2 via m, b
fit g(x) datafile2 using 1:2 via m2, b2

# --- 4. Calcular R manualmente ---
stats datafile1 using 1:2 nooutput
meanx = STATS_mean_x
meany = STATS_mean_y
stats datafile1 using ( (column(1)-meanx)*(column(2)-meany) ) nooutput
covxy = STATS_sum
stats datafile1 using ( (column(1)-meanx)**2 ) nooutput
varx = STATS_sum
stats datafile1 using ( (column(2)-meany)**2 ) nooutput
vary = STATS_sum
R1 = covxy / sqrt(varx * vary)

# Segundo R
stats datafile2 using 1:2 nooutput
meanx = STATS_mean_x
meany = STATS_mean_y
stats datafile2 using ( (column(1)-meanx)*(column(2)-meany) ) nooutput
covxy = STATS_sum
stats datafile2 using ( (column(1)-meanx)**2 ) nooutput
varx = STATS_sum
stats datafile2 using ( (column(2)-meany)**2 ) nooutput
vary = STATS_sum
R2 = covxy / sqrt(varx * vary)

# --- 5. Gráfico ---
set title "Comparación de Regresiones Lineales"
set xlabel "Eje X"
set ylabel "Eje Y"
set grid
set key top left

set terminal pngcairo enhanced font "Arial,12"
set output 'comparacion_regresiones.png'

plot datafile1 using 1:2 title "Datos 1" with points pt 7 lc rgb "blue", \
     f(x) title sprintf("Regresión 1: y=%.2fx+%.2f (R=%.3f)", m, b, R1) with lines lc rgb "blue" lw 2, \
     datafile2 using 1:2 title "Datos 2" with points pt 5 lc rgb "red", \
     g(x) title sprintf("Regresión 2: y=%.2fx+%.2f (R=%.3f)", m2, b2, R2) with lines lc rgb "red" lw 2 dashtype 3

unset output
set terminal wxt

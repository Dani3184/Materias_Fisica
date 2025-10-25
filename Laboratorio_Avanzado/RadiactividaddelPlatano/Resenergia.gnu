# ============================================================
# Resolucion en energia del detector NaI(Tl)
# Ajuste: R(E) = a/sqrt(E) + b y grafico de residuos
# ============================================================

# --- Configuracion General ---
set output "resolucion_energia_residuos.png"
set terminal pngcairo size 1000, 1000 enhanced font "Arial,14"

# Titulo global y configuracion de subgraficos
set multiplot layout 2,1 title "Ajuste de la resolucion en energia del NaI(Tl) y Residuos"

# ------------------------------------------------------------
# --- PARTE SUPERIOR: Datos + ajuste (Resolucion) ---
# ------------------------------------------------------------
set title "Resolucion en Energia del Detector NaI(Tl)"
set xlabel ""                  # Eliminar etiqueta X para el grafico superior
set ylabel "Resolucion (%)"
set xtics format ""            # Ocultar etiquetas X
set grid
set key top right maxrows 1     # Limitar la leyenda

# --- Estilos de Linea ---
set style line 1 lc rgb "#0072BD" pt 7 ps 1.6 lw 2   # Puntos de datos
set style line 2 lc rgb "#D95319" lw 3               # Linea de ajuste
set style line 3 lc rgb "#999999" lt 1 lw 1          # Linea cero/guia

# --- Datos experimentales (Energia en keV, Resolucion en %) ---
$datos << EOD
# E(keV)   R(%)
662    7.443
1173.2 6.4775
1332.5 5.79
302.85 15.36
356    11.39
511    8.342
1274   5.654
EOD

# --- Modelo de ajuste ---
f(x) = a/sqrt(x) + b
# Valores iniciales mas realistas para un mejor fit
a = 60.0
b = 1.0
fit f(x) $datos using 1:2 via a,b

# --- Graficar datos y ajuste ---
set xrange [250:1400]
set yrange [4:17]

plot \
    $datos using 1:2 with points ls 1 title "Datos experimentales", \
    f(x) with lines ls 2 title sprintf("Ajuste: a/√E + b  (a=%.2f, b=%.2f)", a, b)

# ------------------------------------------------------------
# --- PARTE INFERIOR: Residuos (Residuals) ---
# ------------------------------------------------------------

# Cambios de configuracion especificos para el subgrafico de residuos
set title "Residuos (Dato - Ajuste)"
set xlabel "Energia del foton y (keV)"
set ylabel "Residuo (%)"
set xtics format "%g"          # Restablecer formato para mostrar etiquetas X
set yrange [-2:2]              # Rango simetrico para residuos
unset key                      # Quitar leyenda en grafico de residuos

# Dibujar eje en Y=0
set arrow from 250,0 to 1400,0 nohead ls 3

# Graficar residuos DIRECTAMENTE:
# ($2 - f($1)) calcula el residuo para cada punto.
plot $datos using 1:($2 - f($1)) with points ls 1 title "Residuos (dato - ajuste)"

unset multiplot
# --- FIN DEL SCRIPT ---
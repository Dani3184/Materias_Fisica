# --- Configuración general ---
set terminal pngcairo size 1000,700 enhanced font "Arial,14"
set output "resolucion_energia.png"

set title "Resolución en Energía del Detector NaI(Tl)"
set xlabel "Energía del fotón γ (keV)"
set ylabel "Resolución en Energía (%)"
set grid
set key top right

# --- Opciones visuales ---
set style line 1 lc rgb "#0072BD" pt 7 ps 1.8 lw 2   # azul con puntos grandes
set style line 2 lc rgb "#D95319" lw 2 dashtype 2    # línea de ajuste

# --- Datos en línea ---
$datos << EOD
662 7.443
1173.2 6.4775
1332.5 5.79
302.85 15.36
356 11.39
511 8.342
1274 5.654
EOD

# --- Graficar ---
plot $datos using 1:2 with points ls 1 title "Datos experimentales"

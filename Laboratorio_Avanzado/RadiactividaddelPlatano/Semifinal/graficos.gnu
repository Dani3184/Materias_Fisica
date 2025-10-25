# Configuración de la gráfica (opcional pero recomendado)
set title "Comparación de Plátano vs. Fondo"
set xlabel "Channel"
set ylabel "Counts"

# Comando de ploteo corregido con títulos
plot "platanoverdadero.txt" using 1:2 with points title "Plátano", \
     "FondoPlatano" using 1:2 with points title "Fondo"

# Mantener la ventana abierta si lo ejecutas desde un script
pause -1
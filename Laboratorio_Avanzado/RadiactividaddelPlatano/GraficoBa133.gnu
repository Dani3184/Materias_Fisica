# Configuración de Salida a Archivo PNG
set terminal png size 800, 600
set output 'grafico_Ba133.png'

# Configuración del Título y Ejes
set title "Espectro de Bario-133 "
set xlabel "Canal"
set ylabel "Cuentas"
set grid
set key top right
# set logscale y # Sugerencia para ver mejor los picos

# Graficar y Guardar
plot "Ba133Verdadero.txt" using 1:2 with lines lw 2 lc rgb "blue" title "Bario 133"

# No se necesita 'pause -1' porque la terminal es 'png'
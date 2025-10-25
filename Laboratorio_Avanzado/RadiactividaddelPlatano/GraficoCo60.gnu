# Configuración de Salida a Archivo PNG
set terminal png size 800, 600
set output 'grafico_Co60.png'

# Configuración del Título y Ejes
set title "Espectro de Cobalto-60"
set xlabel "Canal"
set ylabel "Cuentas"
set grid
set key top right
# set logscale y # Sugerencia para ver mejor los picos

# Graficar y Guardar
plot "Co60verdader.txt" using 1:2 with lines lw 2 lc rgb "orange" title "Co-60"

# No se necesita 'pause -1' porque la terminal es 'png'
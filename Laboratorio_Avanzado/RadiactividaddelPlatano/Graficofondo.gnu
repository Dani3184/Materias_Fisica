# Configuración de Salida a Archivo PNG
set terminal png size 800, 600
set output 'grafico_fondo_promediado.png'

# Configuración del Título y Ejes
set title "Espectro de Fondo Promediado"
set xlabel "Canal"
set ylabel "Cuentas"
set grid
set key top right

# Graficar y Guardar
plot "fondo_promediado.txt" using 1:2 with lines lw 2 lc rgb "blue" title "Fondo"

# No se necesita 'pause -1' porque la terminal es 'png'
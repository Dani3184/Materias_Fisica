# Configuración de Salida a Archivo PNG
set terminal png size 800, 600
set output 'grafico_Cs137_medicion1.png'

# Configuración del Título y Ejes
set title "Espectro de Cesio-137 (Medición 1)"
set xlabel "Canal"
set ylabel "Cuentas"
set grid
set key top right
# set logscale y # Sugerencia para ver mejor los picos

# Graficar y Guardar
plot "Cs137verdader1.txt" using 1:2 with lines lw 2 lc rgb "red" title "Cs-137 (M1)"

# No se necesita 'pause -1' porque la terminal es 'png'
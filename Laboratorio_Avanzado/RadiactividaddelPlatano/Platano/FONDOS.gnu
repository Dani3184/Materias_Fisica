# 1. Configuración del gráfico
set title "Comparación de Fondos"
set xlabel "Canal"
set ylabel "Cuentas"
set logscale y
set grid
set key top right

# 2. 💾 BLOQUE PARA GUARDAR LA IMAGEN
# gnuplot solo guarda cuando le indicas un terminal de salida (png, jpeg, pdf, etc.)
set terminal pngcairo enhanced font "Arial,12" # Terminal de salida para el archivo
set output 'comparacion_espectros.png'      # Nombre del archivo

# 3. Graficar (Esto guarda la imagen)
plot 'fondoplátano_1.tsv' using 2:3 with steps title "Muestra 1", \
     'fondoplátano_2.tsv' using 2:3 with steps title "Muestra 2"

# 4. 🖼️ VOLVER AL MODO INTERACTIVO
# Debemos cambiar el terminal de vuelta a 'wxt' o 'qt'
unset output                         # Detiene la escritura en el archivo
set terminal wxt title "Comparación de Espectros Limpios" # Vuelve al terminal interactivo
replot                               # Vuelve a dibujar la gráfica en la ventana wxt
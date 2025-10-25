# Configuración del título y etiquetas de los ejes
set title "Energía de ligadura por Nucleón (B.E./A) contra Número de Masa \nModelo de la gota líquida"
set xlabel "Número de nucleones A"
set ylabel "B.E./A MeV"

# Configuración de la leyenda
set key top right

# Configuración del estilo de línea para cada columna
set style line 1 pt 7 ps 1.0 lc rgb "blue" 
set style line 2 pt 5 ps 1.0 lc rgb "red" 

# Comando de graficado: 'plot'
plot 'Energia1.txt' using 1:2 with lines linestyle 1 title "BE/A sin corrección de apareamiento ", \
     ''           using 1:3 with lines linestyle 2 title "BE/A Con corrección de apareamiento"

    # Opcional: guardar automáticamente
set terminal png enhanced
set output "grafico_energia.png"
replot
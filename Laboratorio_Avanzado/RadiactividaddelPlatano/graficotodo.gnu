# Configuración del Título y Ejes
set title "Espectros Individuales y Fondo Promediado"
set xlabel "Canal"
set ylabel "Cuentas"
set grid
set key top right
set logscale y  # Sugerencia: es común usar escala logarítmica para espectros

# Configuración del estilo de línea (opcional, para diferenciar)
set style line 1 lc rgb "blue" lw 2   # Línea azul para Fondo
set style line 2 lc rgb "red" lw 2    # Línea roja para Cs137 (ejemplo)
set style line 3 lc rgb "green" lw 2  # Línea verde para Cs137 (ejemplo)
set style line 4 lc rgb "orange" lw 2 # Línea naranja para Co60 (ejemplo)

# Comando de Graficado (Plot)
# Se usa el operador de continuación de línea (\) para hacer un solo comando 'plot'
plot "fondo_promediado.txt" using 1:2 with lines linestyle 1 title "Fondo Promediado", \
     "fondopromedio2.txt" using 1:2 with lines linestyle 7 title "Fondo Promediado", \
     "Cs137verdader1.txt" using 1:2 with lines linestyle 2 title "Cesio-137 (Medición 1)", \
     "Cs137verdader2.txt" using 1:2 with lines linestyle 3 title "Cesio-137 (Medición 2)", \
     "Co60verdader.txt" using 1:2 with lines linestyle 4 title "Cobalto-60", \
     "Na22Verdadero.txt" using 1:2 with lines linestyle 5 title "Sodio-22", \
     "Ba133Verdadero.txt" using 1:2 with lines linestyle 6 title "Bario-133"

# Pausar para ver el gráfico
pause -1
set title "Espectro de Fondo Promediado"

set xlabel "Canal"

set ylabel "Cuentas"

set grid

set key top right



# Graficar

# plot "fondo_promediado.txt" using 1:2 with lines lw 2 title "Fondo"

# plot "Cs137verdader1.txt" using 1:2 with lines lw 2 title "Fondo"

# plot "Cs137verdader2.txt" using 1:2 with lines lw 2 title "Fondo"

# plot "Co60verdader.txt" using 1:2 with lines lw 2 title "Fondo"
plot "Ba133Verdadero.txt" using 1:2 with lines lw 2 title "Fondo"

# plot "Na22Verdadero.txt" using 1:2 with points title "Fondo"



# Pausar para ver el gráfico

pause -1
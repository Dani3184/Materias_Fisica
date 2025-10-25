reset
set fit quiet    # Evita mensajes largos del ajuste

# =====================================================
# === CONFIGURACIÓN ===
datafile = "regresion.txt"   # 🔹 Cambia este nombre según el archivo
set terminal pngcairo enhanced font "Arial,12"
set grid
set xlabel "Canal"
set ylabel "Energía KeV"
set key top left

# =====================================================
# Definimos la primera recta 7 pts
a1 = 194.0232216
b1 = 0.404006690
R1 = 0.928056 
f1(x) = b1*x + a1
# Segunda recta 4Pts
a2 = 1.489484595
b2 = 0.7128550727
R2 = 0.9999857102
f2(x) = b2*x + a2




# =====================================================
# === 4. Exportar gráfico ===
set title sprintf("Regresión Lineal Epica (%s)", datafile)

# Crear nombre de salida automático según el archivo de entrada
set output sprintf("regresion_epico_%s.png", datafile)

plot datafile using 1:2 title "Puntos de Calibración" with points pt 7 lc rgb "red", \
     f1(x) title sprintf("y1 = %.3fx + %.3f  (R = %.4f)", b1, a1, R1) with lines lw 2 lc rgb "blue", \
     f2(x) title sprintf("y2 = %.3fx + %.3f  (R = %.4f)", b2, a2, R2) with lines lw 3 lc rgb "green"

unset output
set terminal wxt

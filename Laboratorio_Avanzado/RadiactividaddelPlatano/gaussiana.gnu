# ------------------------------------------------------------------
# 1. PARÁMETROS DE FILTRADO Y ARCHIVO DE DATOS
# ------------------------------------------------------------------
# MIN_CANAL = 1392
# MAX_CANAL = 1618
# ARCHIVO_DATOS = "Cs137verdader1.txt" # O el archivo con el pico ya sin fondo
# MIN_CANAL = 2443
# MAX_CANAL = 2770
# ARCHIVO_DATOS = "Co60verdader.txt" # O el archivo con el pico ya sin fondo
# MIN_CANAL = 2834
# MAX_CANAL = 3109
# ARCHIVO_DATOS = "Co60verdader.txt" # O el archivo con el pico ya sin fondo
MIN_CANAL = 660
MAX_CANAL = 768
ARCHIVO_DATOS = "Na22Verdadero.txt" # O el archivo con el pico ya sin fondo
# MIN_CANAL = 1717
# MAX_CANAL = 1849
# ARCHIVO_DATOS = "Na22Verdadero.txt" # O el archivo con el pico ya sin fondo
# MIN_CANAL = 371
# MAX_CANAL = 452
# ARCHIVO_DATOS = "Ba133Verdadero.txt" # O el archivo con el pico ya sin fondo
# MIN_CANAL = 452
# MAX_CANAL = 559
# ARCHIVO_DATOS = "Ba133Verdadero.txt" # O el archivo con el pico ya sin fondo

# ------------------------------------------------------------------
# 2. FUNCIÓN GAUSSIANA SIMPLIFICADA (3 PARÁMETROS)
# f(x) = A * exp(-0.5 * ((x - mu) / sigma)^2) 
# ------------------------------------------------------------------
gauss(x) = A * exp(-0.5 * ((x - mu) / sigma)**2)

# ------------------------------------------------------------------
# 3. ESTIMACIONES INICIALES (¡CRÍTICO!)
# ------------------------------------------------------------------
# *Ajusta estos valores manualmente basado en tu gráfico*
A = 312      # Altura máxima del pico (Amplitud pura)
mu =2900    # Centro del pico (Canal de máxima cuenta)
sigma = 50    # Desviación estándar (Ancho del pico)

# ------------------------------------------------------------------
# 4. AJUSTE NO LINEAL (FIT)
# ------------------------------------------------------------------
# Ajusta solo A, mu, y sigma
fit gauss(x) ARCHIVO_DATOS using 1:2 every ::MIN_CANAL::MAX_CANAL via A, mu, sigma

# ------------------------------------------------------------------
# 5. CONFIGURACIÓN Y GRAFICADO FINAL (Guarda como PNG)
# ------------------------------------------------------------------
set terminal png size 1000, 700 
set output 'ajuste_fotopico_puroCo2.png'

set title "Ajuste Gaussiano (Canales ".MIN_CANAL." a ".MAX_CANAL.")\nResultados del Ajuste"
set xlabel "Canal"
set ylabel "Cuentas (Fondo Restado)"
set grid
set key bottom right

# Muestra los parámetros de ajuste
set label 1 sprintf("A = %.2f\nmu = %.2f\nsigma = %.2f\nChi^2 = %.2e", \
            A, mu, sigma, FIT_WSSR) at graph 0.95, 0.95 right font ",10"

# Grafica los puntos de datos (filtrados) y la función ajustada
plot ARCHIVO_DATOS using 1:2 every ::MIN_CANAL::MAX_CANAL with points pointtype 7 title "Datos Fotopico", \
     gauss(x) with lines linewidth 3 lc rgb "red" title "Ajuste Gaussiano"
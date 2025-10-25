# ------------------------------------------------------------------
# 1. PARÁMETROS DE FILTRADO Y ARCHIVO DE DATOS
# ------------------------------------------------------------------
# MIN_CANAL = 1392
# MAX_CANAL = 1618
# ARCHIVO_DATOS = "Cs137verdader1.txt"
# NOMBRE_ESPECTRO = "Cs-137"
# A = 329
# mu = 1507.92 
# sigma = 42.8651

# MIN_CANAL = 2443
# MAX_CANAL = 2770
# ARCHIVO_DATOS = "Co60verdader.txt"
# NOMBRE_ESPECTRO = "Co-60-P1"
# A = 274
# mu = 2617.71
# sigma = 68.3942

# MIN_CANAL = 2834
# MAX_CANAL = 3109
# ARCHIVO_DATOS = "Co60verdader.txt"
# NOMBRE_ESPECTRO = "Co-60-P2"
# A = 225
# mu = 2974.51
# sigma = 62.1052

# MIN_CANAL = 660
# MAX_CANAL = 768
# ARCHIVO_DATOS = "Na22Verdadero.txt"
# NOMBRE_ESPECTRO = "Na-22-P1"
# A = 212
# mu = 715.549
# sigma = 23.151

# MIN_CANAL = 1717
# MAX_CANAL = 1849
# ARCHIVO_DATOS = "Na22Verdadero.txt"
# NOMBRE_ESPECTRO = "Na-22-P2"
# A = 52
# mu = 1784.27
# sigma = 32.1327

# MIN_CANAL = 380
# MAX_CANAL = 452
# ARCHIVO_DATOS = "Ba133Verdadero.txt"
# NOMBRE_ESPECTRO = "Ba-133-P1"
# A = 1180
# mu = 414.132
# sigma = 20.8221

# MIN_CANAL = 452
# MAX_CANAL = 559
# ARCHIVO_DATOS = "Ba133Verdadero.txt"
# NOMBRE_ESPECTRO = "Ba-133-P2"
# A = 3098
# mu = 502.847
# sigma = 23.3156

MIN_CANAL = 1991
MAX_CANAL = 2148
ARCHIVO_DATOS = "platanoverdadero.txt"
NOMBRE_ESPECTRO = "Platano"
A = 2185
mu = 2063.45
sigma = 30.0942

# ------------------------------------------------------------------
# 2. FUNCIÓN GAUSSIANA
# ------------------------------------------------------------------
gauss(x) = A * exp(-0.5 * ((x - mu) / sigma)**2)

# ------------------------------------------------------------------
# 3. AJUSTE NO LINEAL
# ------------------------------------------------------------------
fit gauss(x) ARCHIVO_DATOS using 1:2 every ::MIN_CANAL::MAX_CANAL via A, mu, sigma

# ------------------------------------------------------------------
# 4. CONFIGURACIÓN Y GRAFICADO FINAL
# ------------------------------------------------------------------
set terminal png size 1000, 700 
set output 'ajuste_'.NOMBRE_ESPECTRO.'.png'

set title "Ajuste Gaussiano - ".NOMBRE_ESPECTRO
set xlabel "Canal"
set ylabel "Cuentas"
set grid
set key bottom right

set label 1 sprintf("A = %.2f\nμ = %.2f\nσ = %.2f", A, mu, sigma) at graph 0.95, 0.95 right

plot ARCHIVO_DATOS using 1:2 every ::MIN_CANAL::MAX_CANAL with points title "Datos", \
     gauss(x) with lines linewidth 2 title "Ajuste Gaussiano"
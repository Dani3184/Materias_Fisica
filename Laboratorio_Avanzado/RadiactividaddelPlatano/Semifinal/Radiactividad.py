import numpy as np
import pandas as pd

# Archivo con los datos del espectro (columna 1: canal, columna 2: cuentas)
# Ejemplo: 'espectro.txt'
datos = np.loadtxt('platanoverdadero.txt', skiprows=1)


canales = datos[:, 0]
cuentas = datos[:, 1]

# Rango del fotopico (ajústalo con tus valores)
canal_min = 1991
canal_max = 2148
# Filtramos los datos dentro del rango
mascara = (canales >= canal_min) & (canales <= canal_max)
cuentas_pico = np.sum(cuentas[mascara])

print(f"Rango del pico: {canal_min} - {canal_max}")
print(f"Cuentas totales en el fotopico: {cuentas_pico:.0f}")
    
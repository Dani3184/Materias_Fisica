import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Nombre del archivo de datos
archivo_datos = 'cuentas.txt'

# --- 1. Cargar los datos desde el archivo de texto ---
try:
    # Leer el archivo, usando espacios como delimitador y sin encabezado
    df = pd.read_csv(archivo_datos, delim_whitespace=True, header=None, names=['fecha', 'hora', 'cuentas'])
    
    # Combinar las columnas de fecha y hora en una sola columna de tipo datetime
    df['timestamp'] = pd.to_datetime(df['fecha'] + ' ' + df['hora'])

except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{archivo_datos}'. Asegúrate de que esté en el mismo directorio.")
    exit()
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    exit()

# --- 2. Agrupar los datos en intervalos de 5 minutos ---
grupos = df.groupby(pd.Grouper(key='timestamp', freq='5T'))

# --- 3. Definir la función para la prueba K-S de Poisson ---
def run_ks_test(data):
    # La lambda de la distribución de Poisson se estima a partir de la media de los datos del grupo.
    # Redondeamos los datos a enteros para la prueba de Poisson.
    data_int = np.round(data).astype(int)
    
    if len(data_int) < 20: # Un mínimo de datos es recomendado para que la prueba tenga sentido
        return None
        
    lambda_estimado = np.mean(data_int)
    
    # La prueba K-S compara la ECDF de los datos con la CDF teórica de Poisson
    statistic, p_value = stats.kstest(data_int, lambda x: stats.poisson.cdf(x, mu=lambda_estimado))
    return p_value

# --- 4. Calcular el valor p para cada grupo de 5 minutos ---
p_values = []
for name, group in grupos:
    p_val = run_ks_test(group['cuentas'])
    if p_val is not None:
        p_values.append(p_val)
        print(f"Intervalo de 5 min: {name} | Número de datos: {len(group)} | Valor p: {p_val:.4f}")

# --- 5. Generar el histograma de los p-valores ---
if len(p_values) > 0:
    plt.figure(figsize=(10, 6))
    plt.hist(p_values, bins=20, edgecolor='black', alpha=0.7)
    plt.title('Histograma de los p-valores de la prueba K-S', fontsize=16)
    plt.xlabel('Valor p')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.axvline(x=0.05, color='red', linestyle='--', label='Nivel de significancia (α=0.05)')
    plt.legend()
    plt.savefig("HistogramKStodo.jpg")
    plt.show()
else:
    print("No se encontraron suficientes intervalos con datos para realizar las pruebas K-S.")
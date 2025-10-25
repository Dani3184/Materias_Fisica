import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Nombre del archivo donde están los datos
nombre_archivo = 'data.txt'

# Valor máximo para mostrar en el histograma
valor_maximo = 150  # Cambia este valor según lo que necesites

try:
    # Leer los datos directamente desde el archivo
    # El 'sep' con la expresión regular r'\s+' maneja múltiples espacios o tabulaciones
    df = pd.read_csv(nombre_archivo, sep=r'\s+', header=None, usecols=[2], names=['conteos'])

    # Convertir la columna de conteos a tipo numérico
    df['conteos'] = pd.to_numeric(df['conteos'])

    # Filtrar los datos hasta el valor máximo
    df_filtrado = df[df['conteos'] <= valor_maximo]

    # ---
    # Cálculo de los estadísticos
    # ---
    print(f"Resumen de estadísticos de los conteos (≤ {valor_maximo}):")
    estadisticos = df_filtrado['conteos'].describe()
    print(estadisticos)
    
    # Adicional: Calcular la moda (valor que más se repite)
    # df['conteos'].mode() devuelve una Serie, por eso usamos .iloc[0] para obtener el primer valor si hay más de uno
    if not df_filtrado['conteos'].mode().empty:
        moda = df_filtrado['conteos'].mode().iloc[0]
        print(f"Moda: {moda:.2f}")

    # ---
    # Creación del Histograma
    # ---
    sns.set_style("whitegrid")
    plt.figure(figsize=(10, 6))

    sns.histplot(df_filtrado['conteos'], kde=True, bins=80, color='purple', alpha=0.7)
    plt.title(f'Distribución de Conteos de Rayos Cósmicos (≤ {valor_maximo}) 🔭', fontsize=16)
    plt.xlabel('Número de Conteos', fontsize=12)
    plt.ylabel('Frecuencia', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Mostrar la gráfica
    plt.show()

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no fue encontrado.")
    print("Asegúrate de que el archivo esté en la misma carpeta que el script.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
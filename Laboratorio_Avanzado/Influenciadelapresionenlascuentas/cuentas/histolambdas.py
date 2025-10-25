import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Nombre del archivo de datos
nombre_archivo = 'estadisticas_5min.csv'

try:
    # Leer el archivo de texto en un DataFrame de pandas
    df = pd.read_csv(nombre_archivo)
    
    # Pedir al usuario los valores mínimo y máximo para el histograma
    print("Por favor, ingrese el rango de valores para el histograma de las medias de cuentas.")
    min_val = 200
    max_val = 1000
    # min_val = float(input("Valor mínimo: "))
    # max_val = float(input("Valor máximo: "))
    
    # Filtrar los datos que están dentro del rango especificado
    datos_filtrados = df[(df['Media'] >= min_val) & (df['Media'] <= max_val)]['Media']
    
    # Verificar si el DataFrame filtrado está vacío
    if datos_filtrados.empty:
        print("No se encontraron datos en el rango especificado. Por favor, intente con otro rango.")
    else:
        # Calcular estadísticas
        media = np.mean(datos_filtrados)
        desviacion_std = np.std(datos_filtrados)
        num_datos = len(datos_filtrados)
        
        # Generar el histograma
        plt.figure(figsize=(12, 7))
        n, bins, patches = plt.hist(datos_filtrados, bins=40, edgecolor='black', alpha=0.7, 
                                  color='skyblue', density=False)
        
        # Añadir líneas de referencia
        plt.axvline(media, color='red', linestyle='--', linewidth=2, label=f'Media: {media:.2f}')
        plt.axvline(media + desviacion_std, color='orange', linestyle=':', linewidth=2, 
                   label=f'+1σ: {media + desviacion_std:.2f}')
        plt.axvline(media - desviacion_std, color='orange', linestyle=':', linewidth=2, 
                   label=f'-1σ: {media - desviacion_std:.2f}')
        
        # Configurar título y etiquetas
        plt.title(f'Histograma de las Medias de Cuentas\n(Rango: {min_val} - {max_val})', fontsize=14, fontweight='bold')
        plt.xlabel('Media de Cuentas', fontsize=12)
        plt.ylabel('Frecuencia', fontsize=12)
        plt.grid(axis='y', alpha=0.3)
        
        # Añadir texto con las estadísticas
        stats_text = f'Número de datos: {num_datos}\nMedia: {media:.2f}\nDesviación estándar: {desviacion_std:.2f}'
        plt.text(0.02, 0.98, stats_text, transform=plt.gca().transAxes, 
                fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        # Añadir leyenda
        plt.legend(loc='upper right')
        
        # Ajustar layout
        plt.tight_layout()
        plt.show()
        
        # Mostrar estadísticas en consola también
        print("\nESTADÍSTICAS DEL HISTOGRAMA:")
        print("=" * 40)
        print(f"Número de datos: {num_datos}")
        print(f"Media: {media:.2f}")
        print(f"Desviación estándar: {desviacion_std:.2f}")
        print(f"Coeficiente de variación: {(desviacion_std/media)*100:.2f}%")
        print(f"Mínimo: {datos_filtrados.min():.2f}")
        print(f"Máximo: {datos_filtrados.max():.2f}")
        print(f"Rango: {datos_filtrados.max() - datos_filtrados.min():.2f}")

except FileNotFoundError:
    print(f"Error: El archivo '{nombre_archivo}' no se encontró. Asegúrese de que el archivo esté en la misma carpeta que el script.")
except ValueError:
    print("Error: Por favor, ingrese números válidos para los valores mínimo y máximo.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
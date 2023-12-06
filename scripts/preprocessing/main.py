import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
sys.path.append('scripts')
from data_acquisition.main import get_dataframe

# # URL del archivo CSV
# urls = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSSFEzwj9erdFwLIxBSLhvBTffcJHX8xpmaebnwqWYkij3DywsUOTZmFvs4QZgOazMi--z9JCFLS_Qt/pub?output=csv"
# df = pd.read_csv(urls)
# print(df)

# # Informacion y descripcion de los datos
# df.info()
# df.describe()

# # filtro columna SORTEO
# df['SORTEO'] = df['SORTEO'].astype(str)
# df['SORTEO'] = df['SORTEO'].apply(lambda x: x.lstrip('Extra ') if x.startswith('Extra ') else x)
# df['SORTEO'] = pd.to_numeric(df['SORTEO'], errors='coerce')

# # filtro columna SORTEO
# df['FECHA'] = pd.to_datetime(df['FECHA'], format='%d/%m/%Y', errors='coerce')
# df = df.dropna(subset=['FECHA'])
# df['FECHA'] = df['FECHA'].dt.strftime('%Y%m%d').astype(int)

# # Dividir la columna Nombre_premio.
# df['PREMIO'] = df['NOMBRE_PREMIO'].str.extract(r'\$([\d,]+) MILLONES', expand=False)
# df['PREMIO'] = pd.to_numeric(df['PREMIO'].str.replace(',', ''), errors='coerce')
# df = df.drop('NOMBRE_PREMIO', axis=1)
# print(df)

# # Variable Objetivo
# numero_ganador = df['NUMERO'].dropna()
# plt.figure(figsize=(12, 6))

# # Histograma
# plt.subplot(1, 2, 1)
# sns.histplot(numero_ganador, kde=True, bins=50)
# plt.title('Distribución de los Números Ganadores')
# plt.xlabel('Número Ganador')
# plt.ylabel('Frecuencia')

# # Boxplot
# plt.subplot(1, 2, 2)
# sns.boxplot(x=numero_ganador)
# plt.title('Boxplot de los Números Ganadores')
# plt.xlabel('Número Ganador')

# plt.tight_layout()
# ruta_guardado = 'C:\\Users\\RTISAS\\Desktop\\CristianParedes\\proyectoUnal\\tdsp_template\\docs\\data\\graficos_loteria.png'
# plt.savefig(ruta_guardado)

# plt.show()


# df['FECHA'] = pd.to_datetime(df['FECHA'])
# # Gráfico para 'NUMERO'
# plt.figure()
# sns.histplot(df['NUMERO'], bins=50, kde=True)
# plt.title('Distribución de NUMERO')
# plt.xlabel('Número Ganador')
# plt.ylabel('Frecuencia')
# plt.savefig('grafico_numero.png')
# plt.close()

# # Gráfico para 'SERIE'
# plt.figure()
# sns.histplot(df['SERIE'], bins=50, kde=True, color='orange')
# plt.title('Distribución de SERIE')
# plt.xlabel('Serie')
# plt.ylabel('Frecuencia')
# plt.savefig('grafico_serie.png')
# plt.close()

# # Gráfico de serie temporal para 'FECHA'
# plt.figure()
# df['FECHA'].value_counts().sort_index().plot(kind='line', color='green')
# plt.title('Frecuencia de Sorteos a lo Largo del Tiempo')
# plt.xlabel('Fecha')
# plt.ylabel('Número de Sorteos')
# plt.savefig('grafico_fecha.png')
# plt.close()

# # Correlación
# correlation_matrix = df[['NUMERO', 'SERIE', 'FECHA']].corr()

# # Visualizando la matriz de correlación
# df['FECHA'] = pd.to_datetime(df['FECHA']).apply(lambda x: x.timestamp())
# correlation_matrix = df[['NUMERO', 'SERIE', 'FECHA']].corr()
# plt.figure(figsize=(8, 6))
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title('Matriz de Correlación')
# ruta_guardado = 'matriz_correlacion.png'
# plt.savefig(ruta_guardado)

# plt.show()

# funcion de limpieza para Árbol de decisión

def cleanDate():
    data = get_dataframe()
    data['FECHA'] = pd.to_datetime(data['FECHA'], errors='coerce')
    lottery_data_cleaned = data.dropna(subset=['FECHA'])
    X = lottery_data_cleaned['FECHA'].map(pd.Timestamp.timestamp).values.reshape(-1, 1)
    y = lottery_data_cleaned['NUMERO'].values

    return X, y
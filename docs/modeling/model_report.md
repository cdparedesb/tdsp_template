# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo final. Es importante incluir los resultados de las métricas de evaluación y la interpretación de los mismos.

## Descripción del Problema

El problema central que se buscó resolver con el modelo final es la predicción de números ganadores en la lotería de Bogotá. Este desafío se enmarca en el contexto de predecir resultados de un juego de azar, donde los números son seleccionados de manera aleatoria en cada sorteo.

El objetivo principal del modelo es explorar si existe alguna tendencia o patrón en los números ganadores que se puedan utilizar para hacer predicciones. Aunque es crucial entender que, debido a la naturaleza aleatoria de la lotería, cualquier patrón observado es probablemente producto de la coincidencia y no implica una previsibilidad real.

## Descripción del Modelo

El modelo final seleccionado para abordar el problema de predecir números ganadores en la lotería de Bogotá es un modelo de series temporales ARIMA (Autoregressive Integrated Moving Average). Este modelo es bien conocido y ampliamente utilizado en el análisis de series temporales por su capacidad para modelar y pronosticar datos temporales basándose en dependencias anteriores.

Para desarrollar y afinar este modelo, se siguió una metodología estructurada que incluyó las siguientes etapas:

+ División de Datos: La serie temporal completa se dividió en conjuntos de entrenamiento y prueba. Se utilizó el 80% inicial de los datos para el entrenamiento (train) y el 20% restante para la prueba (test).

+ Selección de Parámetros: Se realizó un proceso de búsqueda de cuadrícula (Grid Search) para determinar los parámetros óptimos para el modelo ARIMA. Los parámetros en ARIMA son:

    - p (Orden Autoregresivo): Número de términos autoregresivos.
    - d (Orden de Diferenciación): Número de diferenciaciones n-o estacionales requeridas para lograr la estacionariedad.
    - q (Orden del Promedio Móvil): Número de términos de promedio móvil.

+ Se probaron diferentes combinaciones de estos parámetros dentro de los rangos definidos (0 a 2 para cada uno) para encontrar la combinación que minimiza el Criterio de Información de Akaike (AIC), un indicador de la calidad del modelo que penaliza la complejidad.

+ Ajuste del Modelo: Utilizando la combinación óptima de parámetros encontrada (en este caso, p=0, d=1, q=2), se ajustó el modelo ARIMA al conjunto completo de datos de la serie temporal.

+ Pronóstico: Con el modelo ajustado, se realizó un pronóstico para los siguientes 7 pasos temporales (steps=7).

## Evaluación del Modelo

Para evaluar el rendimiento del modelo ARIMA final, se emplearon varias métricas estadísticas comunes en el análisis de series temporales como: 

`Error Cuadrático Medio (MSE)`: Es una medida estándar que calcula el promedio de los cuadrados de los errores, es decir, la diferencia cuadrática entre los valores observados y los pronosticados. Un MSE más bajo indica un mejor rendimiento del modelo.

`Raíz del Error Cuadrático Medio (RMSE)`: Es la raíz cuadrada del MSE y proporciona una medida del error en las mismas unidades que la variable objetivo. Al igual que el MSE, un RMSE más bajo indica un mejor modelo.

## Conclusiones y Recomendaciones

+ Aunque el modelo ARIMA es una herramienta estadística robusta para el análisis de series temporales, su aplicación en la predicción de resultados de la lotería es limitada debido a la naturaleza aleatoria de estos eventos. Las métricas de evaluación proporcionan una visión de la precisión del modelo en términos estadísticos, pero no necesariamente reflejan una capacidad predictiva real en el contexto de la lotería.

+ Los resultados subrayan la naturaleza fundamentalmente aleatoria de los sorteos de lotería. Cada sorteo es un evento independiente, y los patrones percibidos en los datos históricos no son indicativos de resultados futuros.

+ El modelo no puede superar la aleatoriedad inherente de los sorteos de lotería y aunque predice que para los proximos dias es posible que el número ganador sea el 5025 La precisión de las predicciones está limitada por la naturaleza no correlacionada de los datos de la lotería.

## Referencias

1. **Pandas** : [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

2. **Matplotlib**: [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

3. **Statsmodels**:  [Statsmodels Documentation](https://www.statsmodels.org/stable/index.html)


# Reporte del Modelo Final

## Resumen Ejecutivo

En esta sección se presentará un resumen de los resultados obtenidos del modelo final. Es importante incluir los resultados de las métricas de evaluación y la interpretación de los mismos.

## Descripción del Problema

El problema central que se buscó resolver con el modelo final es la predicción de números ganadores en la lotería de Bogotá. Este desafío se enmarca en el contexto de predecir resultados de un juego de azar, donde los números son seleccionados de manera aleatoria en cada sorteo.

El objetivo principal del modelo es explorar si existe alguna tendencia o patrón en los números ganadores que se puedan utilizar para hacer predicciones. Aunque es crucial entender que, debido a la naturaleza aleatoria de la lotería, cualquier patrón observado es probablemente producto de la coincidencia y no implica una previsibilidad real.

## Descripción del Modelo

El modelo final seleccionado para abordar el problema de predecir números ganadores en la lotería de Bogotá es un modelo de árbol de decisión. Este modelo es conocido por su capacidad para modelar complejas relaciones no lineales en los datos.

Para desarrollar y afinar este modelo, se siguió una metodología estructurada que incluyó las siguientes etapas:

+ División de Datos: Se dividió el conjunto de datos en conjuntos de entrenamiento y prueba. Se utilizó el 80% de los datos para el entrenamiento (X_train, y_train) y el 20% restante para la prueba (X_test, y_test).

+ Selección de Parámetros: Se empleó un proceso de búsqueda de cuadrícula (Grid Search) para determinar los parámetros óptimos para el modelo de árbol de decisión. Los parámetros en este modelo son:

    + max_depth (Profundidad Máxima): Profundidad máxima del árbol.
    + min_samples_split (Mínimo de Muestras para Dividir): Número mínimo de muestras requeridas para dividir un nodo.
    + min_samples_leaf (Mínimo de Muestras por Hoja): Número mínimo de muestras requeridas para ser una hoja.
    + Ajuste del Modelo: Utilizando la mejor combinación de parámetros encontrada (max_depth: 3, min_samples_leaf: 1, min_samples_split: 2), se ajustó el modelo de árbol de decisión al conjunto completo de datos de entrenamiento.

## Evaluación del Modelo

Para evaluar el rendimiento del modelo final, se emplearon varias métricas estadísticas comunes en el análisis como por ejemplo: 

`Error Cuadrático Medio (MSE)`: Es una medida estándar que calcula el promedio de los cuadrados de los errores, es decir, la diferencia cuadrática entre los valores observados y los pronosticados. Un MSE más bajo indica un mejor rendimiento del modelo.

`Raíz del Error Cuadrático Medio (RMSE)`: Es la raíz cuadrada del MSE y proporciona una medida del error en las mismas unidades que la variable objetivo. Al igual que el MSE, un RMSE más bajo indica un mejor modelo.

El modelo ajustado fue evaluado utilizando el conjunto de prueba, obteniendo las siguientes métricas:

    + RMSE (Error Cuadrático Medio Raíz): 2920.38
    + MSE (Error Cuadrático Medio): 8565054.70
    + MAE (Error Absoluto Medio): 2538.51
    + R² (Coeficiente de Determinación): -0.00346
    + Score de Explicación: -0.00329

## Conclusiones y Recomendaciones

+ Aunque el modelo de arbol de decisión es una herramienta estadística robusta para la clasificacion y pronosticos, su aplicación en la predicción de resultados de la lotería es limitada debido a la naturaleza aleatoria de estos eventos. Las métricas de evaluación proporcionan una visión de la precisión del modelo en términos estadísticos, pero no necesariamente reflejan una capacidad predictiva real en el contexto de la lotería.

+ Los resultados subrayan la naturaleza fundamentalmente aleatoria de los sorteos de lotería. Cada sorteo es un evento independiente, y los patrones percibidos en los datos históricos no son indicativos de resultados futuros.

+ El modelo no puede superar la aleatoriedad inherente de los sorteos de lotería y aunque predice que para los proximos dias es posible que el número ganador sea el 5025 La precisión de las predicciones está limitada por la naturaleza no correlacionada de los datos de la lotería.

## Referencias

1. **Pandas** : [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)

2. **Matplotlib**: [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)

3. **Statsmodels**:  [Statsmodels Documentation](https://www.statsmodels.org/stable/index.html)


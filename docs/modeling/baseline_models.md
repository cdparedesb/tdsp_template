# Reporte del Modelo Baseline

## Descripción del modelo

Se construye  como punto de referencia o línea base un modelo baseline ARIMA (Autoregressive Integrated Moving Average) es una técnica estadística de modelado de series temporales que se utiliza para pronosticar datos temporales mediante la combinación de tres componentes principales: autoregresión (AR), diferenciación (I) y promedio móvil (MA).

## Variables de entrada

* La variable `FECHA`: fecha en que gano el número se encuentra en formato DD-MM-YYYY.
* Las variables `NÚMERO` Numero ganador del sorteo es de tipo entero categórico.

## Variable objetivo

`Número ganador de la loteria:`  valor futuro de la serie temporal que se está tratando de predecir.

## Evaluación del modelo

### Métricas de evaluación

 Criterio de Información de Akaike AIC: El AIC se utiliza para comparar modelos estadísticos, y su objetivo es encontrar un equilibrio entre el ajuste del modelo a los datos y la complejidad del modelo. Por lo tanto, un modelo con un valor de AIC más bajo se considera preferible.

### Resultados de evaluación

- Mejor modelo ARIMA: order=(0, 1, 2) con Criterio de Información de Akaike AIC=424719.0136663979. Los demas resultados dieron valores mas elevados que el presentado por lo que no se tuvieron en cuenta ya que el AIC entre mas bajo sea mejor es el ajuste de los datos.


## Análisis de los resultados

En este modelo realizado por series de tiempo el hecho de que el AIC de tan elevado indica la complejidad de poder predecir el numero ganador de la loteria. se hace necesario realizar o experimentar con otros modelos e intentar obtener mas datos relacioneados con la loteria de Bogotá.
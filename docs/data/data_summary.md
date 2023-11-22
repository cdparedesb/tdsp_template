# Reporte de Datos


## Resumen general de los datos

El conjunto de datos contiene **28,275 observaciones y 6 variables**.

| Variable | Tipo de dato |
|---|---|
| LOTERIA | Entero |
| SORTEO | Objeto |
| FECHA | Objeto |
| NOMBRE_PREMIO | Objeto |
| NUMERO | Entero |
| SERIE | Entero |

La distribución de las variables es la siguiente:

* **LOTERIA:** La variable `LOTERIA` tiene un **valor único**, `2`.
* **SORTEO:** La variable `SORTEO` tiene un **rango de valores** del `1` al `3000`.
* **FECHA:** La variable `FECHA` tiene un **rango de valores** del `01-01-2014` al `17-12-2022`.
* **NOMBRE_PREMIO:** La variable `NOMBRE_PREMIO` tiene un **rango de valores** de cualquier cadena de caracteres.
* **NUMERO:** La variable `NUMERO` tiene un **rango de valores** del `0` al `9999`.
* **SERIE:** La variable `SERIE` tiene un **rango de valores** del `0` al `449`.

## Resumen de calidad de los datos

Resumen de Calidad de Datos:

**Columna LOTERIA:**

+ No se identificaron problemas en esta columna. Todos los valores son el número 2.

**Columna SORTEO:**

+ Se identificó un registro con letras al inicio ("Extra 00006").
+ Se eliminaron las letras y se mantuvo el número con ceros a la izquierda ("00006").

**Columna Fecha:**

+ Las fechas estaban en formato DD/MM/YYYY y eran de tipo objeto.
+ Se convirtieron a tipo datetime para su manipulación y, si es necesario, se convirtieron a formato numérico.

**Columna NOMBRE PREMIO:**

+ Se dividió la columna en dos nuevas columnas, 'Nombre' y 'Premio', para separar el nombre del premio y su valor monetario.
+ Se extrajo el valor numérico y se creó una nueva columna 'PREMIO'.



## Variable objetivo

La variable objetivo es el número ganador (NUMERO).

Los gráficos muestran la distribución de los números ganadores en los sorteos de la lotería de Bogotá:

![Distribución de los Números Ganadores](data/graficos_loteria.png)

**Histograma:** Esta visualización muestra la frecuencia de cada número ganador. La distribución parece ser bastante uniforme, lo cual es esperado en un juego de azar como la lotería.

**Boxplot:** Este gráfico proporciona una visión de la distribución de los números ganadores, incluyendo la mediana, los cuartiles y los valores atípicos. El boxplot parece ser simétrico, lo que indica que no hay una tendencia clara hacia números más bajos o más altos.

## Variables individuales

Análisis detallado de las variables NUMERO, SERIE y FECHA:

**Gráficos de Distribución**

**NUMERO:** La distribución de los números ganadores es uniforme, lo cual es típico en juegos de azar. No hay una concentración clara hacia números específicos.

![Distribución de los Números](data/grafico_numero.png)

**SERIE:** La distribución de la serie también es bastante uniforme, sin una tendencia clara hacia ciertos números.

![Distribución de las SERIES](data/grafico_serie.png)

**FECHA:** La frecuencia de sorteos a lo largo del tiempo muestra variaciones. Es posible observar picos y caídas en la frecuencia de sorteos en diferentes momentos.

![Distribución de SORTEOS](data/grafico_fecha.png)


## Relación entre variables explicativas y variable objetivo

La correlación entre las variables en el conjunto de datos de la lotería de Bogotá, Se calcula el coeficiente de correlación de Pearson. Este coeficiente mide la relación lineal entre dos variables, y su valor varía entre -1 y 1. Un valor cercano a 1 indica una fuerte correlación positiva, mientras que un valor cercano a -1 indica una fuerte correlación negativa. Un valor cercano a 0 sugiere que no hay una correlación lineal significativa.

Dado que la lotería es un juego de azar, y asumiendo que las variables como NUMERO y SERIE son aleatorias, Se observan correlaciones cercanas a cero entre estas variables.

![Distribución de SORTEOS](data/matriz_correlacion.png)

# Definición de los datos

## Origen de los datos

- La fuente de los datos para este proyecto es el conjunto de datos Resultados Lotería de Bogotá, que se encuentra disponible en la plataforma de datos abiertos de Bogotá. El conjunto de datos contiene información sobre los resultados de todos los sorteos de la Lotería de Bogotá, desde el año 2014 hasta el 2022

## Especificación de los scripts para la carga de datos

- Los datos se obtuvieron descargando el conjunto de datos desde la plataforma de datos abiertos de Bogotá. El conjunto de datos se encuentra en formato CSV, por lo que se pudo importar directamente para el análisis de los datos.

## Referencias a rutas o bases de datos origen y destino

- La ruta o base de datos de origen para los datos es la plataforma de datos abiertos de Bogotá. El conjunto de datos se encuentra disponible para su descarga en el siguiente enlace:

    https://datosabiertos.bogota.gov.co/dataset/resultados-loteria-de-bogota

### Rutas de origen de datos

- Los archivos de origen de los datos se encuentran en la plataforma de datos abiertos de Bogotá, anteriormente descrito.

- Los archivos de origen de los datos tienen la siguiente estructura:

    | Columna | Descripción |
    |---|---|
    | LOTERIA | Loteria de Bogota |
    | SORTEO | Numero de sorteo|
    | FECHA | Fecha del sorteo |
    |NOMBRE DEL PREMIO | Nombre del premio |
    | NÚMERO | número ganador |
    | SERIE | Serie del número ganador |


- Los procedimientos de transformación y limpieza de los datos se realizarán en el entorno de análisis de datos. Los siguientes son los pasos que se llevarán a cabo:

    1. Se importarán los datos del archivo CSV al entorno de análisis de datos.
    2. Se verificará la integridad de los datos, buscando valores atípicos, datos faltantes o errores en la codificación.
    3. Se corregirán los errores encontrados, según sea necesario.
    4. Se crearán nuevas variables, según sea necesario.
    5. Se transformarán los datos para que sean adecuados para el análisis.

### Archivo de datos de destino

- El archivo de destino para los datos será un archivo CSV. Donde se creará y se almacenará en google sheets (Hoja de calculo) para su uso.

- El archivo CSV  tendrá la siguiente estructura:

    | Tabla | Columnas |
    |---|---|
    | sorteos | fecha, tipo, nombre_premio, numero_ganador, serie |

- El procedimiento de carga y transformación de los datos en el archivo CSV de destino se realizarán utilizando las herramientas de administración PANDAS del entorno de análisis de datos. Los siguientes son los pasos que se llevarán a cabo:

    1. Se creará un dataframe o tabla de sorteos.
    2. Se importarán los datos del archivo CSV a la tabla sorteos.
    3. Se ejecutarán los procedimientos de transformación y limpieza de los datos, según se describe anteriormente.

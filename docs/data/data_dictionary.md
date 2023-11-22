# Diccionario de datos

## Tabla: Resultados Lotería de Bogotá

**Fuente de Datos**: Plataforma de Datos Abiertos de Bogotá

**Descripción**: Esta tabla contiene información sobre los resultados de todos los sorteos de la Lotería de Bogotá, desde el año 2014 hasta el año 2022

| Variable | Descripción | Tipo de dato | Rango/Valores posibles | Fuente de datos |
|---|---|---|---|---|
| **LOTERIA** | Indice del Nombre de la lotería | **Entero** | 2 | Plataforma de Datos Abiertos de Bogotá |
| **SORTEO** | Número del sorteo | **Entero** | 1 - 3000 | Plataforma de Datos Abiertos de Bogotá |
| **FECHA** | Fecha del sorteo | **Fecha** | DD-MM-YYYY | Plataforma de Datos Abiertos de Bogotá |
| **NOMBRE DEL PREMIO** | Nombre del premio | **Cadena** | Cualquier cadena de caracteres | Plataforma de Datos Abiertos de Bogotá |
| **NÚMERO** | Número ganador | **Entero** | 0 - 9999 | Plataforma de Datos Abiertos de Bogotá |
| **SERIE** | Serie del número ganador | **Entero** | 0 - 500 | Plataforma de Datos Abiertos de Bogotá |

- **Variable**: nombre de la variable.
- **Descripción**: breve descripción de la variable.
- **Tipo de dato**: tipo de dato que contiene la variable.
- **Rango/Valores posibles**: rango o valores que puede tomar la variable.
- **Fuente de datos**: fuente de los datos de la variable.

## Observaciones:

* Las variables `LOTERIA` y `SORTEO` son variables de identificación.
* La variable `FECHA` se encuentra en formato DD-MM-YYYY.
* Las variables `NOMBRE DEL PREMIO` y `SERIE` son variables categóricas.
* Las variables `NÚMERO` es de tipo entero categórico.



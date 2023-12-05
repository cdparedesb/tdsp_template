# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Modelo Predictor Numeros Loteria
- **Plataforma de despliegue:** 
     El modelo se desplegará localmente en un entorno de Python. Esta configuración permite una integración fácil y directa con aplicaciones y scripts locales de Python, sin la necesidad de configuraciones complejas de servidor o infraestructura en la nube.

- **Requisitos técnicos:** 
    + Python 3.6 o superior.
    + Bibliotecas: 
        * pandas == 2.1.1
        * numpy == 1.26.0
        * scikit-learn == 1.3.0
        * matplotlib == 3.8.2 
        * scipy  ==  0.13.0 

    + Hardware: Depende de la escala del despliegue; para pruebas locales, una computadora estándar es suficiente.

- **Requisitos de seguridad:**  Dado que el modelo se desplegará y utilizará localmente, no hay requisitos específicos de seguridad, como autenticación o encriptación de datos.

- **Diagrama de arquitectura:** 



## Código de despliegue

- **Archivo principal:** `predictor_numeros_loteria.py` Este archivo contiene el código necesario para cargar el modelo entrenado y realizar predicciones basadas en las fechas proporcionadas.
- **Rutas de acceso a los archivos:** 

1. Modelo Entrenado: `tdsp_template\modelo_numeros_loteria.joblib`
ruta donde se encuentra guardado el modelo entrenado que se carga en `predictor_numeros_loteria.py`.
2. Archivo de Datos : https://docs.google.com/spreadsheets/d/e/2PACX-1vSSFEzwj9erdFwLIxBSLhvBTffcJHX8xpmaebnwqWYkij3DywsUOTZmFvs4QZgOazMi--z9JCFLS_Qt/pub?output=csv
- **Variables de entorno:** Para el despligue del modelo de forma Local no es necesario configurar variables de entorno.

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)

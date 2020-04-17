# Madrid

## Requisitos

### Web Framework: Django y Django-Rest
Se ha escogido Django porque proporciona una gran cantidad de herramientas para trabajar con bases de Datos además de su diseño intuitivo.

Se ha escogido Django-Rest como un módulo adicional de Django para poder proporcionar funcionalidad REST a otros servicios que lo requieran en este formato

### Base de Datos:
Se recomienda PostgreSQL. Esta base de datos tiene modulos para trabajar con elementos de posicionamiento y puede integrarse perfectamente con Django.

Sin embargo con el propósito de entregar una herramienta "casi" libre de procesos de instalación se usará SQLite3


## Diseño

### Objetivo 1: Lectura y tratamiento
Esto se implementa descargando el fichero .zip del año 2018 con los datos de contaminación.

Se ha desarrollado un archivo de migración inicial que se baja el archivo directamente de la fuente. Se accede a este archivo directamente desde memoria para agilizar el proceso.

Se recorre cada uno de los archivos .csv y se insertan los datos en la base de datos.
Se han desarrollado 3 Modelos para almacenar los datos:
* Estacion: Contiene los campos "provincia", "municipio" y "estacion"
* DiaMedicion: Contiene los campos "ano", "mes", "dia", "magnitud" y "punto_muestreo". Se añade el campo "estacion" para poder relacionarlo con el elemento Estacion al que pertenece
* HoraMedicion: Contiene los campos "hora", "cantidad" y "validacion". Se añade el campo dia_mediacion para poder relacionarlo con el elemento DiaMedicion al que pertenece

#### Notas:
* Se ha procedido a dividir los datos en distintos modelos para facilitar y agilizar los filtros en el futuro. También se usa un criterio de "Unica fuente de la verdad" ya que si se hubiese puesto toda la información en una sola tabla habrían datos repetidos., Esto puede resultar en procesos tediosos a la hora de realizar cambios en los campos padre, ya que habría que recorrer todos y modificar todos

* No se ha procedido a convertir la fecha en elemento "Date" ya que al haber tomado los datos de una fuente externa a nosotros y que este formato marca un patrón, en el futuro puede será más facil al integrar la aplicación con otras aplicaciones que usen estos mismos datos.

* También el hecho que los datos usen la hora "24" como parte del día entra en contradicción con como Python considera los días, es decir, la hora "24" es considerada por Python como la hora "00" del día siguiente. Esto complicaría muchisimo en el futuro los filtros , ya que hay que tomar en cuenta dos días para filtar lo que Madrid entiende como un día. Otra solución sería meter cada hora como una hora menos, es decir la hora 1 sería la 0 y la hora 24 la 23, esto nos mantendría dentro del mismo día para hacer filtros pero rompe el criterio establecido por la fuente de los datos


## Objetivo 2: Arquitectura
### Tipos de Carga:
#### Masiva

Se incluye el archivo "download_and_load.py" que junto a los archivos de migración puede usarse para cargar datos directamente desde la fuente de datos. De momento la función carga solo los archivos de NO2 del año 2018 pero puede adaptarse facilmente para incluir más magnitudes de medición y otros años


#### En tiempo real
Se usaría la misma función en "download_and_load.py" para cargar datos descargados del archivo "tiempo_real".

Esta función se ejecutaría cada hora usando "Celery y Rabbitmq/Redis" o Cronjobs. Podría crearse una vista en django accesible mediante una url. Esto nos simplificaría el Script de Cron que simplemente tendría la función curl y la url de la vista

#### Datos de temperatura
Se usaría una funcion similar a la anterior. Si es mediante una API habría que adaptar la función a leer archivos JSON o XML, pero la lógica sería la misma


### Explotación:
#### API
Se ha implemantado djangoREST para poder accer a los datos en formato JSON

#### Portal Web
EL motivo de separar los datos en 3 modelos es para simplificar el proceso del portal Web.
Para la visualización de los datos se podrían usar librerias basadas en [d3js](https://d3js.org/) , que es la base para muchisimas librerias de visualización en Javascript

#### Modelo predictivo
EL equipo de Data podrá usar la funcionalidad REST para acceder a los datos

#### Analisis adhoc
EL equipo de Data podrá usar la funcionalidad REST para acceder a los datos


### Volumen de datos
En caso que el volumen de datos sea muy grande siempre se podría migrar los datos a BigQuery.
Es más facil migrar a BigQuery desde PostgreSQL que de datos en bruto.
También podría plantaerse migrar directamente a BigQuery.
BigQuery no es un backend que Django desarrolle de forma nativa. Si al final fuese necesario migrar a BigQuery deberá usarse la API de BigQuery

### Cantidad de Usuarios
Podría plantearse usar herramientas en Google Cloud Platform como Cloud Run que gestiona automaticamente la escalabilidad de la aplicación

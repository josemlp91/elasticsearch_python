# MOTORES DE BÚSQUEDA ESCALABLES CON PYTHON Y ELASTICSEARCH

---

Taller introductorio a Elasticsearch usando Python, impartido por José Miguel López (@josemilop91) como miembro de Python Granada (@pythongranada). 

Durante la charla hablaremos del las dificultades que encontramos cuando implementamos un buscador por texto libre o "full-text", pasando a presentar Elasticsearch, daremos unas pinceladas de algunos conceptos básicos para entender como funcionan sus tripas y ver sus puntos fuertes y no tan fuertes.

Una vez estemos metidos en materia, paseremos a presentar Elasticsearch DSL, que es una librería que nos permite realizar consultas de forma Pythonica a nuestro cluster Elastic. Aquí nos pondremos manos a la obra y veremos ejemplos muy didácticos de como realizar consultas, desde las más básicas a las más complicadas. 

En resumen, vamos a pasar un buen rato hablando de cosas. 

**A fecha de 10 de mayo a las 19:30 en el aula M3 de la Facultad de Ciencias de Granada.**

## Requisitos para que todo funcione perfecto.

- [Docker](https://www.docker.com/community-edition#/download) version **17.03+**
- [Docker Compose](https://docs.docker.com/compose/install/) version **1.6.0+**
- Ganas de aprender.
- Una buena conexión a internet para descargar los recursos.
- Ganas de aprender.

## Contenido del repositorio.

- Transparencias de la charla / taller.
- Ejemplos en Jupyter Notebook.
- Dockerfiles y Docker-Compose

### Docker en Windows

Sí usas Docker desde Windows asegurate que la característica "Shared Drives" se encuentra habilitada para la unidad  `C:`  (Docker for Windows > Settings > Shared Drives). Ver [Configuring Docker for Windows Shared Drives](https://blogs.msdn.microsoft.com/stevelasker/2016/06/14/configuring-docker-for-windows-volumes/) (MSDN Blog).

## Uso

### Arrancar el stack

**Note**: En caso de modificar la imágen base o algun Dockerefile, necesitas ejecutar primero `docker-compose build` .

Iniciar stack usando `docker-compose`:

```console
$ docker-compose up
```

La primera vez se  descargan todas las imágenes y dependencias externas de internet, puede tardar un poco, por favor no te desesperes.

Despues de unos segundos iniciando, puedes acceder a Kibana web UI [http://localhost:5601](http://localhost:5601) con tu navegador web. Para ver nuestros maravillosos ejemplos en Python podemos acceder a la url [http://localhost:8888](http://localhost:8888).

Por defecto este stack expone los siguientes puertos:

- 8888: Jupyter Notebook.

* 5000: Logstash TCP input.
* 9200: Elasticsearch HTTP
* 9300: Elasticsearch TCP transport
* 5601: Kibana UI.

Puede probar a ineyectar un archivo de log en Logstash usando el comando.

```console
$ nc localhost 5000 < /path/to/logfile.log
```



### Cambiar la versión del stack

Cuando desee actualizar la versión del stack. Solo tiene que modificar el número de versión dentro de .env y hacer  **rebuild**  del stack.

```console
$ docker-compose build
$ docker-compose up
```

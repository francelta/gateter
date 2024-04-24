# Proyecto Gateter

Este es un proyecto de Django para administrar gatitos y sus maullidos.

## Instalación

1. Clona este repositorio en tu máquina local usando:

    git clone https://github.com/francelta/gateter.git


2. Navega al directorio del proyecto:

    cd gateter


3. Construye los contenedores Docker y ejecútalos usando Docker Compose:
    
    docker-compose up --build

  
Esto construirá la imagen de Docker necesaria para el proyecto y luego iniciará los contenedores necesarios, incluyendo el servidor web y cualquier otro servicio que haya sido configurado.

## Uso

Una vez que los contenedores de Docker estén en funcionamiento, puedes acceder a la aplicación en tu navegador web en la dirección `http://localhost:8000`.

### Gatitos

En la sección de "Mas Maullidos de Otros Gatitos" podrás ver una lista de todos los gatitos registrados en el sistema. 

## Comandos Útiles de Docker

- Para detener los contenedores Docker, puedes usar:

    docker-compose down
    
- Si necesitas acceder al contenedor donde se ejecuta el servidor web, puedes usar:

    docker-compose exec web bash

## Mantenimiento

Para realizar migraciones de la base de datos después de cambios en los modelos, puedes ejecutar:

    docker-compose exec web python manage.py migrate


Este comando ejecutará las migraciones dentro del contenedor del servidor web.

## Notas

Asegúrate de que los puertos utilizados por los servicios en `docker-compose.yml` estén libres o configúralos según tus necesidades si encuentras conflictos de puertos en tu máquina local.

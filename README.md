# Challenge App

Esta es una aplicación de ejemplo que gestiona la clasificación de bases de datos y envía correos electrónicos basados en la clasificación.

## Requisitos

- Python 3.6+
- pip

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/DrManhattanHack/challengemp_app.git
    cd challengemp_app
    ```

2. Instala las dependencias:

    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal:

    ```sh
    python main.py
    ```

2. Introduce el correo y la contraseña configurada para la aplicación cuando se te solicite.

## Estructura del Proyecto

- `main.py`: Script principal que gestiona la lógica de la aplicación.
- `config.py`: Función para obtener credenciales de correo.
- `database.py`: Gestión de la base de datos.
- `email_sender.py`: Función para enviar correos electrónicos.
- `db_classification.json`: Datos de ejemplo para clasificar bases de datos.
- `user_info.csv`: Información de usuarios de ejemplo.

## Docker

La aplicación también puede ejecutarse dentro de un contenedor Docker. Sigue las instrucciones a continuación para crear y ejecutar la imagen Docker.

### Construir la imagen Docker

```sh
docker build -t challenge_app .

# Challenge App

Esta es una aplicación diseñada para automatizar la revalidación de la clasificación de bases de datos de Mercado Libre. El objetivo es reducir la necesidad de reuniones presenciales para validar la clasificación, enviando correos electrónicos a los managers de las bases de datos más críticas para pedir su confirmación.

## Características

Disponemos de un archivo de tipo JSON con la información de la clasificación de las bases de datos y un archivo CSV con información de usuarios y su manager. El archivo JSON puede tener campos incompletos. En dicho caso, será necesario encontrar alguna solución para procesarlo. El archivo CSV tiene la siguiente forma:

```csv
row_id, user_id, user_state, user_manager
```


## Requisitos

- Python 3.6+
- pip

## Instalación

1. Clona el repositorio:

    ```sh
    git clone https://github.com/DrManhattanHack/challengemp_app.git
    cd challengemp_app
    ```

2. Crea un entorno virtual:

   ```sh
    python -m venv venv
    ```

4. Instala las dependencias:

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
```

### Ejecutar el contenedor Docker

```sh
docker run -it --rm challenge_app
```

### Supuestos

	•	Los datos en el archivo JSON pueden estar incompletos. Se han añadido soluciones para completar datos faltantes con valores predeterminados.
	•	Se asume que los correos electrónicos de los managers están correctos y que el servidor de correo utilizado es Gmail.

### Problemas y Soluciones

	1.	Problema: Datos incompletos en JSON
	•	Solución: Se añaden valores predeterminados para los campos faltantes (db_name, owner_email, classification).
	2.	Problema: Envío de correos fallidos debido a credenciales incorrectas
	•	Solución: Se verifica la autenticación del correo al inicio del programa y se detiene la ejecución si las credenciales son incorrectas.
	3.	Problema: Necesidad de normalizar la base de datos
	•	Solución: Se ha normalizado la base de datos dividiéndola en varias tablas (databases, owners, managers, database_owners_managers) para evitar redundancias.


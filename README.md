# Challenge App

Esta es una aplicación diseñada para automatizar la revalidación de la clasificación de bases de datos de Mercado Libre. El objetivo es reducir la necesidad de reuniones presenciales para validar la clasificación, enviando correos electrónicos a los managers de las bases de datos más críticas para pedir su confirmación.

## Características

La aplicación utiliza dos archivos de entrada: un archivo JSON y un archivo CSV.

### Archivo JSON

El archivo `db_classification.json` contiene información sobre la clasificación de las bases de datos. Cada entrada en este archivo tiene la siguiente estructura:

```json
[
    {
        "db_name": "nombre_de_la_base_de_datos",
        "owner_email": "correo_del_propietario",
        "classification": "clasificación"
    }
]
```
•	db_name: Nombre de la base de datos.

•	owner_email: Correo electrónico del propietario de la base de datos.

•	classification: Clasificación de la base de datos (high, medium, low).

### Archivo CSV

El archivo user_info.csv contiene información sobre los usuarios y sus managers. Tiene la siguiente estructura:

```csv
row_id, user_id, user_state, user_manager
```

•	row_id: Identificador de la fila.

•	user_id: Correo electrónico del usuario (debe coincidir con el owner_email en el archivo JSON).

•	user_state: Estado del usuario (active).

•	user_manager: Correo electrónico del manager del usuario.

Funcionamiento de la Aplicación

1. Lectura y Validación de Datos:
La aplicación lee el archivo JSON y el archivo CSV.
Completa cualquier campo faltante en el archivo JSON con valores predeterminados:
- db_name: "unknown_db"
- owner_email: "unknown@meli.com"
- classification: "unknown"

2. Almacenamiento en Base de Datos:
- Los datos se almacenan en una base de datos SQLite, normalizada en varias tablas (databases, owners, managers, database_owners_managers).

3. Envío de Correos:
- Para cada entrada en la base de datos con clasificación high, se envía un correo al manager del propietario de la base de datos solicitando su confirmación sobre la clasificación.
- El correo se envía utilizando un servidor SMTP (configurado para Gmail).


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
		Solución: Se añaden valores predeterminados para los campos faltantes (db_name, owner_email, classification).
	2.	Problema: Envío de correos fallidos debido a credenciales incorrectas
		Solución: Se verifica la autenticación del correo al inicio del programa y se detiene la ejecución si las credenciales son incorrectas.
	3.	Problema: Necesidad de normalizar la base de datos
		Solución: Se ha normalizado la base de datos dividiéndola en varias tablas (databases, owners, managers, database_owners_managers) para evitar redundancias.


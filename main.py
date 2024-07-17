# main.py
import json
import pandas as pd
from tqdm import tqdm
from colorama import Fore, init, Style
from config import get_email_credentials
from database import create_tables, insert_record, fetch_all_records, engine
from email_sender import send_email
import smtplib

# Inicializar colorama
init(autoreset=True)

# Obtener las credenciales del correo
EMAIL_USER, EMAIL_PASS = get_email_credentials()

print(f"{Fore.GREEN}Usando el correo: {EMAIL_USER}")

# Verificar las credenciales al inicio
try:
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        print(f"{Fore.YELLOW}Verificando credenciales...")
        server.login(EMAIL_USER, EMAIL_PASS)
except smtplib.SMTPAuthenticationError:
    print(f"{Fore.RED}Error: Credenciales del correo mal configuradas.{Style.RESET_ALL}")
    exit(1)
except Exception as e:
    print(f"{Fore.RED}Error al conectar al servidor SMTP: {e}{Style.RESET_ALL}")
    exit(1)

# Leer y completar el archivo JSON
with open('db_classification.json', 'r') as f:
    db_data = json.load(f)

print(f"{Fore.BLUE}Contenido de db_classification.json:")
print(db_data)

# Verificar y completar datos faltantes
for record in db_data:
    if 'db_name' not in record or not record['db_name']:
        record['db_name'] = "unknown_db"
    if 'owner_email' not in record or not record['owner_email']:
        record['owner_email'] = "unknown@meli.com"
    if 'classification' not in record or not record['classification']:
        record['classification'] = "unknown"

# Leer el archivo CSV
user_data = pd.read_csv('user_info.csv')

print(f"{Fore.BLUE}Contenido de user_info.csv:")
print(user_data)

# Crear tablas
create_tables()

# Insertar datos en la base de datos y enviar correos
with engine.connect() as conn:
    trans = conn.begin()
    try:
        for record in tqdm(db_data, desc=f"{Fore.CYAN}Procesando bases de datos", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]"):
            try:
                manager_email = user_data.loc[user_data['user_id'] == record['owner_email'], 'user_manager'].values[0]
                insert_record(conn, record, record['owner_email'], manager_email)
                print(f"{Fore.GREEN}Insertado en la base de datos: {record['db_name']} - {record['owner_email']} - {manager_email} - {record['classification']}")

                # Enviar correos electrónicos para clasificaciones altas
                if record['classification'] == 'high':
                    subject = f"Revalidación de Base de Datos: {record['db_name']}"
                    body = (f"Estimado Manager,\n\n"
                            f"Por favor, confirme la clasificación 'high' de la base de datos {record['db_name']} "
                            f"cuyo owner es {record['owner_email']}. Necesitamos su OK para proceder.\n\n"
                            f"Gracias.")
                    print(f"{Fore.RED}{record['owner_email']} tiene clasificación alta. Enviando correo a {manager_email}...")
                    send_email(EMAIL_USER, EMAIL_PASS, manager_email, subject, body)

            except IndexError:
                print(f"{Fore.RED}No se encontró manager para el usuario: {record['owner_email']}")
                continue
        trans.commit()
    except Exception as e:
        trans.rollback()
        print(f"{Fore.RED}Error durante la inserción de datos: {e}")

# Verificar datos insertados
with engine.connect() as conn:
    rows = fetch_all_records(conn)
    print(f"{Fore.BLUE}Datos insertados en la base de datos:")
    for row in rows:
        print(row)

print(f"{Fore.GREEN}Datos insertados en la base de datos y correos electrónicos enviados")

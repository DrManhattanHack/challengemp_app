# config.py
import getpass
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

def get_email_credentials():
    try:
        EMAIL_USER = input(f"{Fore.YELLOW}Introduce el correo desde el que se solicitará la información: {Style.RESET_ALL}")
        EMAIL_PASS = getpass.getpass(f"{Fore.YELLOW}Introduce la contraseña configurada para el correo: {Style.RESET_ALL}")

        if not EMAIL_USER or not EMAIL_PASS:
            print(f"{Fore.RED}Error: Las credenciales del correo no están configuradas correctamente.{Style.RESET_ALL}")
            raise ValueError("Las credenciales del correo no están configuradas correctamente.")
        
        return EMAIL_USER, EMAIL_PASS
    
    except ValueError as e:
        print(f"{Fore.RED}{e}{Style.RESET_ALL}")
        exit(1)

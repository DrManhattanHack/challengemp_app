# email_sender.py
import smtplib
from email.mime.text import MIMEText
from colorama import Fore

def send_email(from_email, password, to_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            print(f"{Fore.YELLOW}Conectando al servidor SMTP...")
            server.login(from_email, password)
            print(f"{Fore.YELLOW}Enviando correo a {to_email}...")
            server.sendmail(from_email, to_email, msg.as_string())
        print(f"{Fore.GREEN}Correo enviado a {to_email}")
    except Exception as e:
        print(f"{Fore.RED}Error enviando correo a {to_email}: {e}")

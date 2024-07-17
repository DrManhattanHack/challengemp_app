# Utilizar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Configurar DNS
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf

# Copiar los archivos requeridos al contenedor de Docker
COPY requirements.txt requirements.txt
COPY . .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Definir el comando para ejecutar el script
CMD ["python", "main.py"]

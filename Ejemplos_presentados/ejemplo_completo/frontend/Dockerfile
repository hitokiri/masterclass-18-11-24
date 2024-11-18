# Usa una imagen base oficial de Python con Alpine
FROM python:3.12-alpine

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias del sistema necesarias
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copia solo los archivos necesarios para instalar las dependencias
COPY pyproject.toml poetry.lock ./

# Instala las dependencias de Python y actualisar pip
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# Copia el resto del código fuente de la aplicación en el contenedor
COPY . .

# Establece variables de entorno para asegurar que la salida de Python no se almacene en búfer
ENV PYTHONUNBUFFERED=1

# Expone el puerto en el que la aplicación se ejecutará
EXPOSE 8080

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
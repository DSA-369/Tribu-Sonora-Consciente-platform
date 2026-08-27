FROM python:3.11-slim

# Evitar la creación de archivos .pyc y forzar salida inmediata de logs
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Instalar dependencias del sistema necesarias para Reflex y Node
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    unzip \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Instalar librerías de Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY . .

# Inicializar y compilar Reflex
RUN reflex init

# Exponer el puerto del Frontend (3000) y del Backend (8000)
EXPOSE 3000
EXPOSE 8000

# Comando para ejecutar en producción
CMD ["reflex", "run", "--env", "prod"]
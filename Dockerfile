FROM python:3.11-slim-buster

WORKDIR /app

RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env.example .env

# Ejecutar consola
CMD ["python3", "console.py"]

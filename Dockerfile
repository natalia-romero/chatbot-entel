FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env.example .env
COPY main.py ./
COPY db.py ./
COPY locustfile.py ./
COPY memory.py ./
COPY stream.py ./

# Ejecutar consola
CMD ["python3", "console.py"]

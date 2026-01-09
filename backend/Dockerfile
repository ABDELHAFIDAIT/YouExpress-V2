# Image légère de Python
FROM python:3.10-slim

# Empêche Python d'écrire des fichiers .pyc et bufferise la sortie (logs en direct)
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Installation des dépendances système nécessaires pour psycopg2 (Postgres)
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Copie et installation des requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du reste du code
COPY . .

# Le port sur lequel Uvicorn écoute
EXPOSE 8000

# La commande de lancement est gérée par docker-compose, mais on peut mettre une par défaut
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
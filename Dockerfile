# Utiliser une image Python légère
FROM python:3.11-slim  

# Définir le répertoire de travail dans le conteneur
WORKDIR /app 

# Copier les fichiers nécessaires
COPY ./requirements.txt /app/  

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt  

# Copier tout le code source
COPY . /app/  

# Exposer le port 8000
EXPOSE 8000  

# Lancer l'application avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Używamy lekkiej wersji Pythona
FROM python:3.10-slim

# Instalujemy biblioteki systemowe potrzebne dla OpenCV (to częsty problem w Dockerze!)
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Ustawiamy katalog roboczy wewnątrz kontenera
WORKDIR /app

# Kopiujemy plik z wymaganymi bibliotekami
COPY requirements.txt .

# Instalujemy biblioteki Pythonowe
RUN pip install --no-cache-dir -r requirements.txt

# Kopiujemy cały Twój kod do kontenera
COPY . .

# Domyślna komenda (zostanie nadpisana w docker-compose, ale warto ją mieć)
CMD ["python", "main.py"]
# 1. Utilitzem una imatge base oficial i molt lleugera de Python
FROM python:3.12-slim

# 2. Establim el directori de treball dins del contenidor
WORKDIR /app

# 3. Copiem el fitxer de dependències primer (Optimització de la memòria cau de Docker)
COPY requirements.txt .

# 4. Instal·lem les dependències
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiem tota la resta del codi de l'aplicació
COPY . .

# 6. Exposem el port on s'executarà el servidor intern
EXPOSE 8000

# 7. La comanda exacta per arrancar l'API quan s'engegui el contenidor
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
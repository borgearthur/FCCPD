FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expõe a porta 80 (padrão HTTP)
EXPOSE 80

CMD ["python", "app.py"]
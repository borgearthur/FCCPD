FROM python:3.10-slim

WORKDIR /app

COPY app/database.py /app/database.py

RUN apt-get update && apt-get install -y sqlite3

CMD ["python", "database.py"]
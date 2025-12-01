import os
import redis
import psycopg2
from flask import Flask

app = Flask(__name__)

REDIS_HOST = os.getenv('REDIS_HOST', 'cache')
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('POSTGRES_DB')
DB_USER = os.getenv('POSTGRES_USER')
DB_PASS = os.getenv('POSTGRES_PASSWORD')

cache = redis.Redis(host=REDIS_HOST, port=6379)

def get_db_version():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return db_version[0]
    except Exception as e:
        return f"Erro ao conectar no DB: {str(e)}"

@app.route('/')
def hello():
    count = cache.incr('hits')
    
    db_status = get_db_version()
    
    return f"""
    <h1>Desafio Docker Compose</h1>
    <p><b>Cache (Redis):</b> Esta página foi vista {count} vezes.</p>
    <p><b>Database (Postgres):</b> {db_status}</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
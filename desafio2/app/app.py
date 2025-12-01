import sqlite3
import os
from datetime import datetime

DB_PATH = '/dados/meu_banco.sqlite'
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    """Inicializa o banco e cria a tabela se não existir."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acessos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_acesso TEXT
        )
    ''')
    conn.commit()
    return conn

def registrar_acesso(conn):
    """Insere o timestamp atual no banco."""
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO acessos (data_acesso) VALUES (?)", (agora,))
    conn.commit()
    print(f"✅ Novo acesso registrado: {agora}")

def ler_dados(conn):
    """Lê e imprime todos os acessos salvos."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM acessos")
    registros = cursor.fetchall()
    
    print("\n--- Histórico de Acessos (Persistência) ---")
    if not registros:
        print("Nenhum registro encontrado.")
    else:
        for reg in registros:
            print(f"ID: {reg[0]} | Data: {reg[1]}")
    print("-------------------------------------------\n")

if __name__ == "__main__":
    print("Iniciando aplicação...")
    try:
        conexao = init_db()
        registrar_acesso(conexao)
        ler_dados(conexao)
        conexao.close()
    except Exception as e:
        print(f"Erro: {e}")
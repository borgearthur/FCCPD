import os
import requests
from flask import Flask

app = Flask(__name__)

# URL do Serviço A (Pega da variável de ambiente ou usa localhost como fallback)
# Nota: 'service-a' é o nome do container na rede Docker
SERVICE_A_URL = os.getenv('SERVICE_A_URL', 'http://service-a:3000/api/users')

@app.route('/')
def dashboard():
    try:
        # Comunicação HTTP entre microsserviços
        response = requests.get(SERVICE_A_URL)
        users = response.json()
        
        # Processamento dos dados (Lógica de negócio do Serviço B)
        html_output = "<h1>Painel de Usuários (Microsserviço B)</h1><ul>"
        
        for user in users:
            html_output += f"<li><b>{user['name']}</b> está ativo desde <u>{user['joined_at']}</u>.</li>"
            
        html_output += "</ul>"
        return html_output
        
    except requests.exceptions.ConnectionError:
        return "<h1>Erro</h1><p>Não foi possível comunicar com o Serviço A.</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
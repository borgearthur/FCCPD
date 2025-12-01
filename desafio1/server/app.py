from flask import Flask
import datetime
import socket

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    hostname = socket.gethostname()
    return f"[Server {hostname}] Resposta recebida às {now}\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
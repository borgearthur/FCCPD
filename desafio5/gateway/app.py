import os
import requests
from flask import Flask, request, jsonify, Response

app = Flask(__name__)

USERS_SERVICE_URL = os.getenv('USERS_SERVICE_URL', 'http://users-service:3000')
ORDERS_SERVICE_URL = os.getenv('ORDERS_SERVICE_URL', 'http://orders-service:5000')

def proxy_request(service_url, path):
    """
    Função auxiliar que encaminha a requisição para o serviço de destino.
    """
    try:
        target_url = f"{service_url}/{path}"
        
        resp = requests.request(
            method=request.method,
            url=target_url,
            headers={key: value for (key, value) in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False
        )

        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items()
                   if name.lower() not in excluded_headers]

        return Response(resp.content, resp.status_code, headers)

    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Service unavailable"}), 503

@app.route('/users', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/users/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway_users(path):
    return proxy_request(USERS_SERVICE_URL, path)

@app.route('/orders', defaults={'path': ''}, methods=['GET', 'POST', 'PUT', 'DELETE'])
@app.route('/orders/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway_orders(path):
    return proxy_request(ORDERS_SERVICE_URL, path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
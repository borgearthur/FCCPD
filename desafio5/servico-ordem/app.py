from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_orders():
    return jsonify({
        "service": "Orders Service",
        "data": [
            { "id": 101, "item": "Notebook", "price": 2500 },
            { "id": 102, "item": "Mouse Gamer", "price": 150 }
        ]
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
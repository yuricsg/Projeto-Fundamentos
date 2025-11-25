import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

USERS_URL = os.getenv("USERS_URL", "http://service-users:6001")
ORDERS_URL = os.getenv("ORDERS_URL", "http://service-orders:6002")

@app.route("/users")
def proxy_users():
    try:
        resp = requests.get(f"{USERS_URL}/users", timeout=3)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"erro": f"Falha ao acessar service-users: {e}"}), 500

@app.route("/orders")
def proxy_orders():
    try:
        resp = requests.get(f"{ORDERS_URL}/orders", timeout=3)
        resp.raise_for_status()
        return jsonify(resp.json())
    except Exception as e:
        return jsonify({"erro": f"Falha ao acessar service-orders: {e}"}), 500

@app.route("/summary")
def summary():
    try:
        users = requests.get(f"{USERS_URL}/users", timeout=3).json()
        orders = requests.get(f"{ORDERS_URL}/orders", timeout=3).json()
    except Exception as e:
        return jsonify({"erro": f"Falha ao acessar serviços: {e}"}), 500

    users_by_id = {u["id"]: u["nome"] for u in users}
    summary_list = [
        {
            "order_id": o["id"],
            "user_id": o["user_id"],
            "user_name": users_by_id.get(o["user_id"], "desconhecido"),
            "valor": o["valor"],
        }
        for o in orders
    ]
    return jsonify(summary_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
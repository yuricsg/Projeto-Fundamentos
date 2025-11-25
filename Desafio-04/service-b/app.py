import os
from flask import Flask, jsonify
import requests

app = Flask(__name__)

SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://service-a:5000")

@app.route("/relatorio")
def relatorio():
    try:
        resp = requests.get(f"{SERVICE_A_URL}/users", timeout=3)
        resp.raise_for_status()
        users = resp.json()
    except Exception as e:
        return jsonify({"erro": f"Falha ao chamar service-a: {e}"}), 500

    frases = [
        f"Usuário {u['nome']} ativo desde {u['ativo_desde']}"
        for u in users
    ]
    return jsonify({"mensagens": frases})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
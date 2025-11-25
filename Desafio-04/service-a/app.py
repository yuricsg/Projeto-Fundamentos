from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "nome": "Elon", "ativo_desde": "2021-05-10"},
    {"id": 2, "nome": "Mark", "ativo_desde": "2022-01-03"},
    {"id": 3, "nome": "Donald", "ativo_desde": "2023-07-21"},
]

@app.route("/users")
def get_users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
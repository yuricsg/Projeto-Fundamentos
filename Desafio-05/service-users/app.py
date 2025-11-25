from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "nome": "Cristiano Ronaldo"},
    {"id": 2, "nome": "Lionel Messi"},
    {"id": 3, "nome": "Neymar Jr"},
]

@app.route("/users")
def get_users():
    return jsonify(USERS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)
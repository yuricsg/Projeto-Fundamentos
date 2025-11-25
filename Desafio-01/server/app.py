from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"Olá servidor Flask! Hora do servidor: {now}\n"

if __name__ == "__main__":
    # Escutar em todas as interfaces dentro do container, porta 8080
    app.run(host="0.0.0.0", port=8080)
import os
import time
from datetime import datetime

from flask import Flask, jsonify
import psycopg2
import redis

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "exemplo")
DB_USER = os.getenv("DB_USER", "user")
DB_PASS = os.getenv("DB_PASS", "password")

REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

def get_db_conn():
    return psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
    )

def get_redis():
    return redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

@app.route("/")
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # cache: contador de acessos
    r = get_redis()
    hits = r.incr("hits")

    # db: ler registros da tabela "pessoas"
    try:
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute("SELECT id, nome FROM pessoas ORDER BY id;")
        rows = cur.fetchall()
        cur.close()
        conn.close()
    except Exception as e:
        rows = []
        app.logger.error(f"Erro ao acessar o banco: {e}")

    return jsonify(
        {
            "mensagem": "Aplicação web falando com db e cache",
            "hora": now,
            "acessos_cache": hits,
            "pessoas_db": [{"id": r[0], "nome": r[1]} for r in rows],
        }
    )

if __name__ == "__main__":
    time.sleep(5)
    app.run(host="0.0.0.0", port=8080)
CREATE TABLE IF NOT EXISTS pessoas (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);

INSERT INTO pessoas (nome) VALUES ('Estevao'), ('Yamal'), ('Mbappe');
CREATE TABLE IF NOT EXISTS pessoas (
    id SERIAL PRIMARY KEY,
    nome TEXT NOT NULL
);

INSERT INTO pessoas (nome) VALUES ('Lewis Hamilton'), ('Max Verstappen'), ('Carlos Sainz');
# Desafio 3 — Docker Compose Orquestrando Serviços

## Objetivo

Usar Docker Compose para orquestrar múltiplos serviços dependentes:
uma aplicação web, um banco de dados e um cache.

## Serviços:

- **web**: aplicação Flask (porta interna 8080, exposta como 8083 no host).
- **db**: PostgreSQL, inicializado com a tabela `pessoas`.
- **cache**: Redis, usado como contador de acessos.

Todos os serviços estão na mesma rede interna `desafio3-net`.

## Docker Compose

Principais pontos do `docker-compose.yml`:

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: exemplo

  cache:
    image: redis:7

  web:
    build: ./web
    depends_on:
      - db
      - cache
    environment:
      DB_HOST: db
      DB_NAME: exemplo
      DB_USER: user
      DB_PASS: password
      REDIS_HOST: cache
      REDIS_PORT: 6379

networks:
  desafio3-net:
    driver: bridge
```

- `depends_on` garante que `db` e `cache` sejam iniciados antes de `web`.
- As variáveis de ambiente informam ao `web` como se conectar ao `db` e ao `cache`.
- A rede `desafio3-net` permite que os serviços se enxerguem pelos nomes `db`, `cache` e `web`.

## Como executar

Na pasta `Desafio-03`:

```bash
docker compose up --build
```

Acesse:

```bash
curl http://localhost:8083/
```

ou abra `http://localhost:8083/` no navegador.

A resposta JSON mostra:

- contador de acessos vindo do Redis (`acessos_cache`);
- lista de pessoas vinda do PostgreSQL (`pessoas_db`).

## Comunicação entre serviços

- `web` → `db`: via hostname `db`, porta 5432, usando `psycopg2`.
- `web` → `cache`: via hostname `cache`, porta 6379, usando a biblioteca `redis`.
- Todos conectados na rede interna `desafio3-net`.

## Prints dos resultados:
![1](https://github.com/user-attachments/assets/2dc8daf5-f4b3-4baf-b449-a01b5e0f92eb)

![2](https://github.com/user-attachments/assets/6f73c5c3-dac2-4a7b-b130-5bf0e42bee55)

![3](https://github.com/user-attachments/assets/914823a9-a0fa-46b9-b25d-16fcd31ab29c)


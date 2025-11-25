# Desafio 4 — Microsserviços Independentes

## Arquitetura

- **service-a** (porta 5000): expõe `GET /users`, retornando uma lista de usuários em JSON.
- **service-b** (porta 5001): expõe `GET /relatorio`, chama `service-a` via HTTP,
  combina as informações e devolve frases como “Usuário X ativo desde ...”.

Ambos têm Dockerfiles próprios e são orquestrados por `docker-compose.yml`
em uma rede interna `desafio4-net`.

## Como executar

```bash
docker compose up --build
```

Testar:

```bash
curl http://localhost:5000/users
curl http://localhost:5001/relatorio
```
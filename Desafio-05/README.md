# Desafio 5 — Microsserviços com API Gateway

## Arquitetura

- **service-users**: `/users` → lista de usuários.
- **service-orders**: `/orders` → lista de pedidos.
- **gateway**: ponto único de entrada:
  - `/users` → encaminha para `service-users`.
  - `/orders` → encaminha para `service-orders`.
  - `/summary` → exemplo extra combinando usuários e pedidos.

Todos os serviços são containers Docker orquestrados por `docker-compose.yml`
na rede interna `desafio5-net`. Apenas o `gateway` é exposto ao host (porta 7000).

## Como executar

```bash
docker compose up --build
```

Testar via gateway:

```bash
curl http://localhost:7000/users
curl http://localhost:7000/orders
curl http://localhost:7000/summary
```
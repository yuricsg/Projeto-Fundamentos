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

## Prints dos resultados:

### /users:
<img width="1221" height="181" alt="rota_users" src="https://github.com/user-attachments/assets/e89e73c1-8cf0-4b57-8ed3-edc7cb475cf5" />

### /orders:
<img width="1218" height="164" alt="rota_orders" src="https://github.com/user-attachments/assets/3ff34153-0d8f-44c2-bea2-5d22b8e9865f" />

### /summary:
<img width="1182" height="191" alt="rota_summary" src="https://github.com/user-attachments/assets/db89a3f5-7f0c-4428-a263-499c58f1a716" />

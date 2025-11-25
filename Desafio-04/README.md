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

## Print dos resultados:
### Microsserviço A
<img width="1233" height="166" alt="microsserviço a" src="https://github.com/user-attachments/assets/59931414-dcd0-4cac-909b-9a5076db29e4"/>

### Microsserviço B
<img width="1361" height="196" alt="microsserviço b" src="https://github.com/user-attachments/assets/58844b6b-ae10-442f-8f7a-c7c87f080b29" />

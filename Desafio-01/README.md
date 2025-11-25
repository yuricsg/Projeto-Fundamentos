# Desafio 1 — Containers em Rede

Disciplina: Fundamentos de Computação Concorrente, Paralela e Distribuída

## Objetivo

Criar dois containers que se comunicam por uma rede Docker customizada:
- Um container executa um servidor web (Flask) na porta 8080.
- Outro container realiza requisições HTTP periódicas para o servidor (curl em loop).

## Arquitetura

- `server/`: contém o servidor Flask.
  - `app.py`: código do servidor web.
  - `Dockerfile`: imagem do servidor.
- `client/`: contém o cliente HTTP.
  - `client.sh`: script que faz requisições periódicas.
  - `Dockerfile`: imagem do cliente.
- `docker-compose.yml`: define a rede Docker customizada e os serviços.

## Rede Docker

A rede customizada é definida em `docker-compose.yml`:

```yaml
networks:
  minha-rede-customizada:
    driver: bridge
```

Os dois serviços (`server` e `client`) são conectados a essa rede, permitindo que o cliente acesse o servidor pelo hostname `server` na porta `8080`.

## Como executar

1. Certifique-se de ter o Docker instalado e o Docker Desktop em execução.
2. Na pasta do projeto, execute:

```bash
docker compose up --build
```

3. Observe os logs do cliente mostrando as respostas do servidor.
4. (Opcional) Acesse `http://localhost:8080` no navegador para ver a resposta diretamente.

Para encerrar:

```bash
docker compose down
```

## Demonstração da comunicação

Os logs do cliente no terminal mostram as requisições HTTP sendo feitas periodicamente e as respostas retornadas pelo servidor Flask, comprovando a comunicação entre os containers pela rede Docker customizada.
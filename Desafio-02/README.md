# Desafio 2 — Volumes e Persistência

## Objetivo

Demonstrar persistência de dados usando volumes Docker com um banco PostgreSQL.

## Arquitetura

- `docker-compose.yml`: define o serviço `db` (PostgreSQL) e o volume `pgdata-desafio2`.
- `db/init.sql`: cria a tabela `pessoas` e insere alguns registros iniciais.

## Volume de dados

No `docker-compose.yml`:

```yaml
volumes:
  pgdata-desafio2:
```

Esse volume é montado no container em:

```yaml
- pgdata-desafio2:/var/lib/postgresql/data
```

Assim, mesmo que o container seja removido, os arquivos de dados continuam no volume.

## Como executar

Subir o banco:

```bash
docker compose up -d
```

Consultar os dados:

```bash
docker exec -it desafio2-postgres psql -U user -d exemplo -c "SELECT * FROM pessoas;"
```

## Teste de persistência

1. Suba o container e consulte a tabela `pessoas`.
2. Pare e remova o container (sem remover volumes):

```bash
docker compose down
```

3. Suba novamente:

```bash
docker compose up -d
```

4. Consulte novamente:

```bash
docker exec -it desafio2-postgres psql -U user -d exemplo -c "SELECT * FROM pessoas;"
```

Os mesmos registros estarão presentes, demonstrando que os dados persistem no volume
`pgdata-desafio2` mesmo após a remoção e recriação do container.
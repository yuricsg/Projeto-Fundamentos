#!/bin/sh

SERVER_URL="http://server:8080"  # 'server' será o nome do serviço/host na rede Docker

echo "Iniciando cliente. Enviando requisições para $SERVER_URL a cada 5 segundos"

while true; do
  echo "--------------------------------------------------"
  echo "[$(date)] Fazendo requisição para o servidor..."
  curl -s $SERVER_URL
  echo
  sleep 5
done
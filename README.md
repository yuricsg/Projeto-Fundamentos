# Projeto – Fundamentos de Computação Concorrente, Paralela e Distribuída

Repositório criado para a disciplina **Fundamentos de Computação Concorrente, Paralela e Distribuída**, com o objetivo de praticar conceitos de **containers**, **comunicação entre serviços**, **orquestração com Docker Compose** e **arquiteturas baseadas em microsserviços e API Gateway**.

Cada desafio está organizado em uma pasta própria e possui seu **próprio README** com detalhes de implementação, arquitetura, comandos de execução e prints de funcionamento.

---

## Estrutura do Repositório

- `Desafio-01/` – **Containers em Rede**  
	Dois containers em uma rede Docker customizada:  
	- servidor web (Flask) na porta 8080;  
	- cliente que realiza requisições HTTP periódicas ao servidor.  
	Demonstração de comunicação entre containers e logs de troca de mensagens.  
	README próprio com explicação da arquitetura, passos de execução e prints.

- `Desafio-02/` – **Volumes e Persistência**  
	Container com banco de dados (PostgreSQL) utilizando **volumes** Docker para armazenar dados fora do container.  
	Demonstração de que os dados persistem mesmo após remoção e recriação do container.  
	README próprio explicando o uso de volumes, testes de persistência e evidências.

- `Desafio-03/` – **Docker Compose Orquestrando Serviços**  
	Aplicação composta por três serviços: **web**, **db** (PostgreSQL) e **cache** (Redis).  
	Orquestração com `docker-compose.yml`, uso de `depends_on`, rede interna e variáveis de ambiente.  
	README próprio descrevendo a arquitetura, a comunicação entre serviços e como executar os testes.

- `Desafio-04/` – **Microsserviços Independentes**  
	Dois microsserviços HTTP independentes:  
	- **Service A**: expõe uma lista de usuários em JSON;  
	- **Service B**: consome o Service A e exibe informações combinadas (ex.: “Usuário X ativo desde ...”).  
	Cada serviço possui seu próprio Dockerfile, garantindo isolamento.  
	README próprio documentando endpoints, fluxo de chamadas e comandos de execução.

- `Desafio-05/` – **Microsserviços com API Gateway**  
	Arquitetura com **API Gateway** centralizando o acesso a dois microsserviços:  
	- **service-users**: fornece dados de usuários;  
	- **service-orders**: fornece pedidos;  
	- **gateway**: expõe `/users`, `/orders` e `/summary`, orquestrando as chamadas aos serviços.  
	Todos os serviços são executados como containers via Docker Compose.  
	README próprio com explicação detalhada da arquitetura e exemplos de testes via gateway.

---

## Como Navegar pelos Desafios

Cada pasta (`Desafio-01`, `Desafio-02`, `Desafio-03`, `Desafio-04`, `Desafio-05`) contém:

- um `docker-compose.yml` (quando aplicável);
- os serviços/containers específicos daquele desafio;
- um `README.md` com:
	- objetivo do desafio;
	- explicação da arquitetura;
	- passos para execução (`docker compose up --build`, comandos de teste, etc.);
	- prints/resultados quando necessário.

Para entender ou executar um desafio específico, basta entrar na pasta correspondente e seguir as instruções do README local.

---

## Tecnologias Utilizadas

- **Docker** e **Docker Compose**
- **Python** + **Flask** para serviços web e gateways
- **PostgreSQL** para banco de dados
- **Redis** para cache
- Scripts de shell e comandos de terminal para demonstração de uso de containers, redes e volumes.

Essas tecnologias foram usadas para ilustrar, na prática, conceitos de concorrência, paralelismo e distribuição, com foco em **comunicação entre processos**, **isolamento**, **orquestração de serviços** e **persistência de dados** em ambientes conteinerizados.

---

## Autoria

Este repositório foi desenvolvido como parte das atividades da disciplina **Fundamentos de Computação Concorrente, Paralela e Distribuída**.

- **Autor:** Yuri França  
- **Instituição:** CESAR School  
# Portfólio de Desafios Docker & Microsserviços

Este repositório contém a resolução prática de 5 desafios focados em Containerização (Docker), Orquestração (Docker Compose) e Arquitetura de Microsserviços.

## Identificação
**Aluno:** Arthur de Assis Borges
**Curso/Disciplina:** FCCPD

## Estrutura do Projeto

O projeto está organizado em diretórios independentes para cada desafio, contendo seus respectivos códigos-fonte, Dockerfiles e documentação específica.

* [`/desafio1`](./desafio1) - **Containers em Rede:** Comunicação básica entre cliente e servidor via rede bridge.
* [`/desafio2`](./desafio2) - **Volumes e Persistência:** Banco de dados com persistência de dados pós-destruição de container.
* [`/desafio3`](./desafio3) - **Orquestração com Compose:** Aplicação Node.js com Redis orquestrada via Docker Compose.
* [`/desafio4`](./desafio4) - **Microsserviços Independentes:** Comunicação HTTP direta entre dois serviços (Provider/Consumer).
* [`/desafio5`](./desafio5) - **API Gateway:** Implementação de um Gateway Nginx centralizando o acesso a microsserviços.

## Pré-requisitos Gerais

Para executar os projetos, é necessário ter instalado:
* [Docker Engine](https://docs.docker.com/engine/install/)
* [Docker Compose](https://docs.docker.com/compose/install/)

## Tecnologias Utilizadas
* Docker & Docker Network
* Python (Flask)
* Node.js
* Nginx (Reverse Proxy)
* PostgreSQL & Redis
* Shell Scripting

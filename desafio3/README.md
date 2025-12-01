# Desafio 3: Orquestração com Docker Compose

Este projeto demonstra a orquestração de três serviços interdependentes utilizando Docker Compose.

## Arquitetura

A solução é composta por três contêineres que se comunicam através de uma rede interna isolada (`minha_rede`):

1.  **Web (Python/Flask):** O front-end da aplicação. Ele processa as requisições HTTP na porta 5000.
2.  **DB (PostgreSQL):** Banco de dados relacional para persistência.
3.  **Cache (Redis):** Armazenamento em memória para contagem de acessos rápida.

### Fluxo de Dados
1. O usuário acessa `localhost:5000`.
2. O serviço **Web** conecta-se ao **Cache** (hostname: `cache`) para incrementar o contador de visitas.
3. O serviço **Web** conecta-se ao **DB** (hostname: `db`) para verificar a versão do banco de dados.
4. O resultado é retornado ao usuário.

## Como Rodar

1. Certifique-se de ter o Docker e o Docker Compose instalados.
2. Na raiz do projeto, execute:

```bash
docker-compose up --build
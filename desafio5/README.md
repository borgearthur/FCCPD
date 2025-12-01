# Desafio 5: Arquitetura de Microsserviços com API Gateway (Python)

Este projeto implementa o padrão **API Gateway** de forma programática utilizando **Python e Flask**. O Gateway atua como um Proxy Reverso, centralizando a entrada de requisições e roteando-as para os microsserviços apropriados.

## Arquitetura

A aplicação é composta por 3 containers rodando na mesma rede interna:

1.  **API Gateway (Python):** Ponto único de entrada (Porta 8080). Recebe requisições e as encaminha (proxy) para os serviços internos.
2.  **Users Service (Node.js):** API interna de usuários.
3.  **Orders Service (Python):** API interna de pedidos.

### Fluxo da Requisição
1. Cliente acessa `localhost:8080/users`.
2. Gateway intercepta, identifica a rota e faz uma requisição interna para `users-service:3000`.
3. A resposta é capturada pelo Gateway e devolvida ao cliente.

## Estrutura do Projeto

* `/gateway`: Aplicação Flask que gerencia o roteamento.
* `/servico-user`: API Node.js.
* `/servico-ordem`: API Python/Flask.
* `docker-compose.yml`: Define a topologia e injeta as URLs dos serviços no Gateway.

## Como Executar

1.  Na raiz do projeto, execute:
    ```bash
    docker-compose up --build
    ```
2.  Os serviços internos (`ms_users` e `ms_orders`) iniciarão, seguidos pelo Gateway.

## Endpoints Públicos

O acesso direto aos microsserviços é bloqueado externamente. Todo acesso deve passar pelo Gateway na porta **8080**:

| Rota | Destino Interno | Descrição |
| :--- | :--- | :--- |
| `http://localhost:8080/users` | `users-service:3000` | Retorna JSON de usuários. |
| `http://localhost:8080/orders` | `orders-service:5000` | Retorna JSON de pedidos. |

## Diferencial Técnico (Custom Gateway)

Diferente de usar um proxy estático (como Nginx), este Gateway é uma aplicação Python completa. Isso permite:
* **Lógica Personalizada:** Manipulação de headers e transformação de respostas antes de entregar ao cliente.
* **Segurança Centralizada:** Facilidade para implementar autenticação (ex: validar tokens) em um único lugar (`app.py`) antes de repassar a requisição.
* **Robustez:** Uso da biblioteca `requests` para gerenciar a comunicação HTTP interna.
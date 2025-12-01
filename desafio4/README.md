# Desafio 4: Microsserviços Independentes (Poliglota)

Este projeto demonstra a comunicação entre dois microsserviços desenvolvidos em linguagens diferentes, rodando em containers isolados e orquestrados pelo Docker Compose.

## Arquitetura

A solução utiliza uma arquitetura **Producer/Consumer**:

1.  **Service A (Node.js):** Atua como a fonte da verdade (API de Usuários). Retorna dados brutos em JSON.
2.  **Service B (Python/Flask):** Atua como frontend/consumidor. Ele faz uma requisição HTTP interna para o Service A, processa os dados e renderiza HTML para o usuário final.

### Diagrama de Comunicação
`[Navegador]` -> (HTTP) -> `[Service B (Python)]` -> (HTTP Interno) -> `[Service A (Node)]`

## Estrutura de Pastas

* `/servicoA`: Código do microsserviço Node.js (Porta 3000).
* `/servicoB`: Código do microsserviço Python (Porta 5000).
* `docker-compose.yml`: Orquestração e definição da rede `microservices-net`.

## Como Executar

1.  Certifique-se de estar na pasta raiz do desafio.
2.  Execute o comando:
    ```bash
    docker-compose up --build
    ```
3.  Aguarde até ver os logs indicando que ambos os serviços estão rodando.

## Endpoints e Testes

| Serviço | URL (Host) | Descrição |
| :--- | :--- | :--- |
| **Service B (Principal)** | `http://localhost:5000` | Exibe a lista formatada em HTML (Consome o Service A). |
| **Service A (Debug)** | `http://localhost:3000/api/users` | Exibe o JSON bruto dos usuários. |

## Detalhes Técnicos

* **Service Discovery:** O Serviço B encontra o Serviço A utilizando o nome do container (`service-a`) como hostname, resolvido pelo DNS interno do Docker.
* **Variáveis de Ambiente:** A URL do serviço A não está fixa no código. Ela é injetada no container Python via variável `SERVICE_A_URL` no `docker-compose.yml`.
* **Isolamento:** Cada serviço possui seu próprio `Dockerfile` com dependências específicas (Node vs Python).
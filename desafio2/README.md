Desafio 2 — Persistência de Dados (SQLite + Docker Volumes)
Este projeto demonstra como garantir a persistência de dados em aplicações Dockerizadas. Ele utiliza um script Python que grava registros de acesso em um banco de dados SQLite.

O objetivo é mostrar que, sem um Volume Docker, os dados são perdidos quando o container é destruído. Com o volume configurado corretamente, o histórico de acessos é mantido.

Estrutura do Projeto

Dockerfile: Configura o ambiente Python, instala o SQLite3 e define o comando de execução.

app/database.py: Script principal que gerencia o banco de dados. Ele:

Cria o banco em /dados/meu_banco.sqlite.

Registra um novo acesso com timestamp atual.

Lê e exibe todo o histórico de acessos salvo no banco.

Pré-requisitos
Docker instalado e em execução.

Como Executar
1. Preparação (Correção do Nome do Arquivo)
O Dockerfile espera um arquivo chamado database.py. Renomeie seu arquivo fonte:

Bash

mv app/app.py app/database.py
2. Construir a Imagem
Na raiz do projeto (onde está o Dockerfile):

Bash

docker build -t imagem-persistente .
3. Testando a Persistência
Cenário A: Sem Persistência (Errado)
Se rodarmos o container sem mapear volumes, os dados serão salvos apenas dentro do container efêmero.

Rode o container:

Bash

docker run --rm imagem-persistente
Rode novamente:

Bash

docker run --rm imagem-persistente
Resultado: Você verá apenas 1 registro (o atual) em cada execução. O histórico anterior foi perdido.

Cenário B: Com Persistência (Volume Bind Mount)
O script Python salva o banco na pasta /dados. Precisamos mapear essa pasta para o nosso computador.

Crie uma pasta local para guardar os dados:

Bash

mkdir dados_locais
Rode o container mapeando o volume (-v):

Bash

# Sintaxe: -v <caminho_host>:<caminho_container>
docker run --rm -v $(pwd)/dados_locais:/dados imagem-persistente
Execute o comando acima várias vezes. Resultado: A cada execução, a lista de "Histórico de Acessos" crescerá, pois o arquivo meu_banco.sqlite está sendo salvo na sua pasta dados_locais.

Saída Esperada (Com Persistência)
Após rodar o container 3 vezes usando o volume, o console deve mostrar:

Plaintext

Iniciando aplicação...
Novo acesso registrado: 2025-10-27 10:00:03

--- Histórico de Acessos (Persistência) ---
ID: 1 | Data: 2025-10-27 09:55:10
ID: 2 | Data: 2025-10-27 09:58:22
ID: 3 | Data: 2025-10-27 10:00:03
-------------------------------------------
Detalhes Técnicos
Caminho do Banco: O script força a criação do diretório /dados caso ele não exista (os.makedirs).


Dockerfile: Utiliza a imagem leve python:3.10-slim e instala explicitamente o pacote sqlite3 via apt-get para garantir compatibilidade.
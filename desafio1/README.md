Desafio 1 — Containers em Rede
Comunicação entre Containers Docker (Python Server + Client Script)
Este projeto demonstra a comunicação entre dois containers Docker isolados, conectados através de uma bridge network personalizada. O projeto consiste em um servidor HTTP simples (Flask) e um cliente que realiza requisições contínuas (cURL).

 Estrutura do Projeto
Server: Uma aplicação Python Flask que responde com o nome do host e o horário atual.

Client: Um script Shell rodando em Alpine Linux que faz requisições a cada 5 segundos para o servidor.

 Pré-requisitos
Docker instalado e em execução.

 Como Executar
Siga os passos abaixo para construir e rodar o ambiente.

1. Criar a Rede Docker
Primeiro, criamos uma rede para que os containers possam se enxergar pelo nome (DNS interno do Docker).

Bash

docker network create rede-desafio
2. Construir as Imagens
Construir a imagem do Servidor: O servidor utiliza a imagem base python:3.10-slim e expõe a porta 8080.

Bash

cd server
docker build -t imagem-servidor .
cd ..
Construir a imagem do Cliente: O cliente utiliza a imagem base alpine:latest com curl instalado.

Bash

cd client
docker build -t imagem-cliente .
cd ..
3. Executar os Containers
Passo A: Iniciar o Servidor Atenção: O script do cliente está configurado para buscar o endereço http://meu-servidor:8080. Portanto, é obrigatório nomear o container ou definir o alias de rede como meu-servidor.

Bash

docker run -d --name meu-servidor --network rede-desafio imagem-servidor
Passo B: Iniciar o Cliente O cliente executará o script script.sh automaticamente ao iniciar.

Bash

docker run --name container-cliente --network rede-desafio imagem-cliente
Resultado Esperado
No terminal onde o cliente está rodando, você verá o seguinte loop de mensagens a cada 5 segundos:

Plaintext

Iniciando cliente de requisições...
Alvo: http://meu-servidor:8080
---
Enviando request...
[Server <id-do-container>] Resposta recebida às HH:MM:SS
Nota: A resposta do servidor não é um JSON, mas sim uma string formatada contendo o hostname e o horário.

Detalhes dos Arquivos
server/app.py: Código Python que define a rota /. Retorna uma string f-string com socket.gethostname() e datetime.

client/script.sh: Loop while true que imprime "Enviando request..." e executa o comando curl.

Dockerfiles: Configurações mínimas para instalar as dependências (flask no server, curl no client) e definir os comandos de entrada (CMD).
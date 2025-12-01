echo "Iniciando cliente de requisições..."
echo "Alvo: http://meu-servidor:8080"

while true; do
  echo "---"
  echo "Enviando request..."
  curl http://meu-servidor:8080
  sleep 5
done
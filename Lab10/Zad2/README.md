docker swarm init

docker stack deploy -c docker-compose.yml gallery

docker-compose -f docker-compose.yml -f docker-compose-update.yml --log-level ERROR config > stack.yml

docker stack deploy -c stack.yml gallery

docker swarm leave --force
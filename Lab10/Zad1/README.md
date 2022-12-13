docker swarm init

docker image build -t zad1 .

docker service create --detach --replicas 1 zad1

docker swarm leave --force
# apiserver
Local API Python Server

# SETUP COMMANDS
> cd docker/apidocker/
> sudo docker run --name apiserver apiserverimage:1.0
> sudo docker network create my_network
> sudo docker run -p 5000:5000 --network my_network --name apiserver  apiserverimage:1.0
> cd docker/apicaller
> sudo docker run --name apiserver apicallerimage:1.0
> sudo docker run --network my_network --name apicaller apicallerimage:1.0

# pull docker image
sudo docker pull vsdpsingh/vishwadeep:apidocker1.0
# run docker image
sudo docker run -p 5000:5000 --name apiserver --network my_network vsdpsingh/vishwadeep:apidocker1.0
# login docker image
sudo docker exec -it apiserver bash
# check what all containers running
sudo docker ps -a

# api caller
# build container
sudo docker build -t vsdpsingh/vishwadeep:apicaller1.0 .
# run container
sudo docker run --name apicaller --network my_network vsdpsingh/vishwadeep:apicaller1.0

# for docker-compose
sudo docker-compose up
sudo docker-compose down
sudo docker-compose up --build

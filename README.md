# apiserver
Local API Python Server

# pull docker image
sudo docker pull vsdpsingh/vishwadeep:apidocker1.0
# run docker image
sudo docker run -p 5000:5000 --name apiserver vsdpsingh/vishwadeep:apidocker1.0
# login docker image
sudo docker exec -it apiserver bash
# check what all containers running
sudo docker ps -a

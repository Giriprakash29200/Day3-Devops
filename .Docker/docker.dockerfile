docker pull httpd  # Docker pull httpd web server from Dockerhub 

docker ps -a  # this command show currently running docker containers

docker images # this command show current images

docker run -it --name "webserver" -p "80:80" httpd  # this command for running image to container 

docker exec -it 'CONTAINER ID' /bin/bash #Executeing the docker container

docker commit "CONTAINER ID" "NAME OF tag" #this command for using container to image

docker save -o ./myimage.tar "IMAGE NAME"  # this command using for saving image to tar file 

docker push "DOCKER HUB USER NAME" "FILENAME" tag  # this command for using to push the docker image to docker hub



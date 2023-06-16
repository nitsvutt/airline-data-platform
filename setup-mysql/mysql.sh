#!/bin/sh

docker network create -d bridge mysql

docker run --name mysql -d \
    -p 3306:3306 \
    -e MYSQL_USER=kafka \
    -e MYSQL_PASSWORD=password \
    -e MYSQL_ROOT_PASSWORD=admin \
    -v /Users/trantrieuvu/Desktop/mysql:/var/lib/mysql \
    --network mysql \
    --restart always\
    mysql:latest

docker exec -it mysql mysql -u root -p
#!/bin/sh

openssl rand -base64 756 > /Users/trantrieuvu/Desktop/mongodb-keyfile/security.keyFile

chmod 400 /Users/trantrieuvu/Desktop/mongodb-keyfile/security.keyFile

docker network create -d bridge mongodb

docker run --name mongodb -d \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=root \
    -e MONGO_INITDB_ROOT_PASSWORD=admin \
    -v /Users/trantrieuvu/Desktop/mongodb1:/data/db \
    mongo:latest

docker exec -it mongo-1 mongosh -u root -p admin | cat init.sh
# note that you should exit the current session and log in again after the restart process finished

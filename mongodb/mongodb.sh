#!/bin/sh

docker network create -d bridge mongodb

docker run --name mongodb -d \
    -p 27017:27017 \
    -e MONGO_INITDB_ROOT_USERNAME=root \
    -e MONGO_INITDB_ROOT_PASSWORD=admin \
    -v /Users/trantrieuvu/Desktop/mongodb:/data/db \
    mongo:latest

docker exec -it mongo-1 mongosh | cat init.sh

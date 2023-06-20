#!/bin/sh

docker network create -d bridge cassandra

docker run --name cassandra -d \
    -p 9042:9042 \
    -v /Users/trantrieuvu/Desktop/cassandra:/var/lib/cassandra \
    --network cassandra \
    --restart always \
    cassandra:latest

docker cp /Users/trantrieuvu/Documents/Workspace/airline-data-platform/setup-cassandra/cassandra.yaml cassandra:/etc/cassandra/

docker exec -it cassandra cqlsh --request-timeout=6000
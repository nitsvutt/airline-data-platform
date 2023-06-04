#!/bin/sh

docker run --name mysql -d \
    -p 3306:3306 \
    -e MYSQL_USER=user \
    -e MYSQL_PASSWORD=password \
    -e MYSQL_ROOT_PASSWORD=admin \
    -v /Users/trantrieuvu/Desktop/mysql:/var/lib/mysql \
    mysql:latest
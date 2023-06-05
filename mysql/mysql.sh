#!/bin/sh

docker run --name mysql -d \
    -p 3306:3306 \
    -e MYSQL_USER=kafka \
    -e MYSQL_PASSWORD=password \
    -e MYSQL_ROOT_PASSWORD=admin \
    -v /Users/trantrieuvu/Desktop/mysql:/var/lib/mysql \
    mysql:latest

# grant all privileges on flight_delay.* to 'kafka';
# /bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mysql --from-beginning
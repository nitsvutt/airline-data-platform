#!/bin/sh

docker exec -it connect bash

(echo 1; sleep 20; echo y; sleep 20; echo y; sleep 20; echo y) | /bin/confluent-hub install confluentinc/kafka-connect-jdbc:10.7.1
(echo 1; sleep 20; echo y; sleep 20; echo y; sleep 20; echo y) | /bin/confluent-hub install mongodb/kafka-connect-mongodb:1.10.0

cd /usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc/
curl -O https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar
~/../../etc/confluent/docker/run
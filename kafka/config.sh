#!/bin/sh

docker exec -it connect bash

/bin/confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.7.1
/bin/confluent-hub install --no-prompt mongodb/kafka-connect-mongodb:1.10.0
/bin/confluent-hub install --no-prompt confluentinc/kafka-connect-avro-converter:7.4.0

cd /usr/share/confluent-hub-components/confluentinc-kafka-connect-jdbc/
curl -O https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar
~/../../etc/confluent/docker/run

# /bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic mysql --from-beginning
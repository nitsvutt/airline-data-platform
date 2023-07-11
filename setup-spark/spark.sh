#!bin/sh

# install openjdk 11
brew install openjdk@11

# install scala
brew install scala

# install pyenv for python versions management
brew install pyenv
# install python (on only this project)
pyenv install 3.10.4
# set this version for the project
pyenv local 3.10.4

# install apache spark
cd ~/Documents/Workspace/tools
wget https://dlcdn.apache.org/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz
tar -xzf spark-3.3.2-bin-hadoop3.tgz

# export pyspark driver to use python in ~/.bash_profile
"""
export SPARK_HOME=~/Documents/Workspace/tools/spark-3.3.2-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin
export PYSPARK_PYTHON=python
export PYSPARK_DRIVER_PYTHON=python
"""

# export pyspark driver to use jupyter in ~/.zshrc
"""
export SPARK_HOME=~/Documents/Workspace/tools/spark-3.3.2-bin-hadoop3
export PATH=$PATH:$SPARK_HOME/bin
export PYSPARK_DRIVER_PYTHON=jupyter
export PYSPARK_DRIVER_PYTHON_OPTS='notebook'
"""

cd ~/Documents/Workspace/tools/spark-jars
# download mysql connector
wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar
# download mongodb connector
wget https://repo1.maven.org/maven2/org/mongodb/spark/mongo-spark-connector_2.11/2.4.0/mongo-spark-connector_2.11-2.4.0.jar
# download bigquery connector
wget https://storage.googleapis.com/spark-lib/bigquery/spark-3.3-bigquery-0.31.1.jar

# add packages to connect to databases
pyspark --packages mysql:mysql-connector-java:8.0.30,org.mongodb.spark:mongo-spark-connector_2.11:2.4.0,com.datastax.spark:spark-cassandra-connector_2.12:3.3.0,com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.31.1
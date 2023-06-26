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
brew install apache-spark

# export pyspark driver to jupyter in ~/.bash_profile
"""
export SPARK_HOME=/opt/homebrew/Cellar/apache-spark/3.4.1/libexec
export PYSPARK_PYTHON=python
export PYSPARK_DRIVER_PYTHON=python
"""

# add package to connect to cassandra
pyspark --packages com.datastax.spark:spark-cassandra-connector_2.12:3.3.0


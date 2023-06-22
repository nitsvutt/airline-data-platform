#!bin/sh

# download the official homebrew formula for mongodb and the database tools
brew tap mongodb/brew

# install mongodb
brew install mongodb-community

# create 3 data folders for 3 replicas
mkdir -p ~/Desktop/mongos/db1
mkdir -p ~/Desktop/mongos/db2
mkdir -p ~/Desktop/mongos/db3

# set up 3 replicas
mongod --port 2717 --dbpath ~/Desktop/mongos/db1 --replSet myReplicaSet
mongod --port 2727 --dbpath ~/Desktop/mongos/db2 --replSet myReplicaSet
mongod --port 2737 --dbpath ~/Desktop/mongos/db3 --replSet myReplicaSet

# connect to one replica
mongosh --port 2717

# stop replicaset
mongosh --port 2737 --eval 'db.adminCommand("shutdown");'
mongosh --port 2727 --eval 'db.adminCommand("shutdown");'
mongosh --port 2717 --eval 'db.adminCommand("shutdown");'





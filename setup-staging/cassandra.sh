#!bin/sh

# install cassandra
brew install cassandra

# change authenticator mode to PasswordAuthenticator and increase timeout by 10 times
open /opt/homebrew/etc/cassandra/cassandra.yaml

# login with cassandra user
cqlsh -u cassandra -p cassandra --request-timeout=6000

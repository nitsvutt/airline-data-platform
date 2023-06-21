#!bin/sh

# install mysql
brew install mysql

# start mysql
brew services start mysql

# set up password for mysql
mysql_secure_installation # enter your password and check all no

# stop mysql
brew services stop mysql

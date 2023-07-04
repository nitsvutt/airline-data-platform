#!bin/sh

### set up database
# create root user (psql command)
create role root with login password 'admin';
create database metabase_data;
grant all on database metabase_data to root;
\c metabase_data
grant all on schema public to root;


# export environment varriables
export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabase_data
export MB_DB_PORT=5432
export MB_DB_USER=root
export MB_DB_PASS=admin
export MB_DB_HOST=localhost

### set up metabase
# get jar file
cd ~/Desktop/metabase/
wget https://downloads.metabase.com/v0.46.6/metabase.jar

# run this file
java -jar metabase.jar
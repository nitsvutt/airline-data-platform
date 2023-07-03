# get jar file
cd ~/Desktop/metabase/
wget https://downloads.metabase.com/v0.46.6/metabase.jar

# set up posgresql to store metabase data
brew install postgresql

# create root user
# psql command
create role root with login password 'admin';
create database metabase_app;
grant all privileges on database metabase_app to root;

# set up database
export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabase_data
export MB_DB_PORT=5432
export MB_DB_USER=root
export MB_DB_PASS=admin
export MB_DB_HOST=localhost

# run this file
java -jar metabase.jar
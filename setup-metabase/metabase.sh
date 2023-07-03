# get jar file
cd ~/Desktop/metabase/
wget https://downloads.metabase.com/v0.46.6/metabase.jar

# set up database
createdb metabaseappdb
export MB_DB_TYPE=postgres
export MB_DB_DBNAME=metabaseappdb
export MB_DB_PORT=5432
export MB_DB_USER=root
export MB_DB_PASS=admin
export MB_DB_HOST=localhost

# run this file
java -jar metabase.jar
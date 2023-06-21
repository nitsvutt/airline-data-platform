---MYSQL
-- create an auto incremental id
alter table flight_records add id int primary key auto_increment;

---MONGODB


---CASSANDRA
--create a keyspace
create keyspace flight_delay with replication = {'class':'SimpleStrategy', 'replication_factor':1};

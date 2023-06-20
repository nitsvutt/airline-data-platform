---MYSQL
-- grant privileges for the user
grant all privileges on flight_delay.* to 'kafka';

-- create an auto incremental id
alter table flight_records add id int primary key auto_increment;

-- create a source table
create table source as select * from flight_records limit 1000000;

---MONGODB
--create a source table
db.flight_records.find().limit(1000000).forEach(function(docs){db.source.insert(docs);})

---CASSANDRA
--create a keyspace
create keyspace flight_delay with replication = {'class':'SimpleStrategy', 'replication_factor':1};

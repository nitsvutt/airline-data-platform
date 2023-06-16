---MYSQL
-- grant privileges for the user
grant all privileges on flight_delay.* to 'kafka';

-- change datatype of 'EntryDate' column to datetime
alter table flight_records modify EntryDate datetime;

-- create a source table
create table source as select * from flight_records limit 1000000;

-- create a sink table
create table sink like source;

---MONGODB
--create a test table
db.source.insertMany(db.flight_records.find().limit(1000000).toArray());

db.flight_records.find().limit(1000000).forEach(function(docs){db.source.insert(docs);})

---CASSANDRA
--create a keyspace
create keyspace flight_delay with replication = {'class':'SimpleStrategy', 'replication_factor':1};
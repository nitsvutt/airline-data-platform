-- create admin user
create role root with superuser = true and login = true and password = 'admin';

-- create keyspace with 3 replicas
create keyspace flight_delay with replication = {'class': 'SimpleStrategy', 'replication_factor': 1};

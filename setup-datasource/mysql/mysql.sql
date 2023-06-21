-- create database flight_delay in order to load data to
create database if not exists flight_delay;

-- create an auto incremental id
alter table flight_records add id int primary key auto_increment;
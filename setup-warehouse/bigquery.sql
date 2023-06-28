-- create schema flight_delay
create schema if not exists `flight_delay`;

--create table dim_date
create or replace table `flight_delay.dim-date`(
  id INT64 not null,
  flight_delay DATE,
  year INT64,
  quarter INT64,
  month INT64,
  dayofmonth INT64,
  dayofweek INT64
);

-- create table dim_airline
create or replace table `flight_delay.dim_airline`(
  id INT64 not null,
  reporting_airline STRING,
  dot_id_reporting_airline INT64,
  iata_code_reporting_airline STRING,
  tail_number STRING,
  flight_number_reporting_airline INT64
)

-- create table dim_

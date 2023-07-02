-- create schema flight_delay
create schema if not exists `flight_delay`;

--create table dim_date
create or replace table `flight_delay.dim_date`(
  id INT64,
  year INT64,
  quarter INT64,
  month INT64,
  day_of_month INT64,
  day_of_week INT64,
  flight_date DATE
);

-- create table dim_airline
create or replace table `flight_delay.dim_airline`(
  id INT64,
  reporting_airline STRING,
  dot_id_reporting_airline INT64,
  iata_code_reporting_airline STRING,
  tail_number STRING,
  flight_number_reporting_airline INT64
);

-- create table dim_origin
create or replace table `flight_delay.dim_origin`(
  id INT64,
  origin_airport_id INT64,
  origin_airport_seq_id INT64,
  origin_city_market_id INT64,
  origin STRING,
  origin_city_name STRING,
  origin_state STRING,
  origin_state_fips INT64,
  origin_state_name STRING,
  origin_wac INT64
);

-- create table dim_destination
create or replace table `flight_delay.dim_destination`(
  id INT64,
  dest_airport_id INT64,
  dest_airport_seq_id INT64,
  dest_city_market_id INT64,
  dest STRING,
  dest_city_name STRING,
  dest_state STRING,
  dest_state_fips INT64,
  dest_state_name STRING,
  dest_wac INT64
);

-- create table dim_schedule
create or replace table `flight_delay.dim_schedule`(
  id INT64,
  crs_dep_time INT64,
  dep_time_block STRING,
  crs_arr_time INT64,
  arr_time_block STRING,
  crs_elapsed_time INT64,
  distance INT64,
  distance_group INT64
);

-- create table dim_cancellations_and_diversions
create or replace table `flight_delay.dim_cancellations_and_diversions`(
  id INT64,
  cancelled INT64,
  cancellation_code STRING,
  diverted INT64
);

-- create table fact_records
create or replace table `flight_delay.fact_records`(
  id INT64,
  date_id INT64,
  airline_id INT64,
  origin_id INT64,
  destination_id INT64,
  schedule_id INT64,
  cancellations_and_diversions_id INT64,
  dep_time INT64,
  dep_delay INT64,
  dep_delay_minutes INT64,
  dep_delay_15 INT64,
  dep_delay_groups INT64,
  taxi_out INT64,
  taxi_in INT64,
  wheels_off INT64,
  wheels_on INT64,
  arr_time INT64,
  arr_delay INT64,
  arr_delay_minutes INT64,
  arr_delay_15 INT64,
  arr_delay_groups INT64,
  actual_elapsed_time INT64,
  air_time INT64,
  flights INT64,
  carrier_delay INT64,
  weather_delay INT64,
  nas_delay INT64,
  security_delay INT64,
  late_aircraft_delay INT64
);
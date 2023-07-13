# import libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# initialize spark session
spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("StagingToWarehouse") \
        .config("spark.executor.memory", "2g") \
        .config("spark.executor.cores", '2') \
        .config("spark.driver.memory", '2g') \
        .config("spark.driver.cores", '2') \
        .config("spark.cassandra.connection.host", "localhost") \
        .config("spark.cassandra.connection.port", "9042") \
        .config("spark.cassandra.auth.username", "root") \
        .config("spark.cassandra.auth.password", "admin") \
        .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
        .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", "../../tools/bigquery/key_file.json") \
        .getOrCreate()

# get max id of fact_records table
fact_records_max_id = spark.read \
                        .format("bigquery") \
                        .options(parentProject="test-373705") \
                        .options(table="flight_delay.fact_records") \
                        .load().select("id") \
                        .agg(max("id")) \
                        .collect()[0][0]
# ensure max id have a value
if fact_records_max_id is None:
    fact_records_max_id=-1

# extract data from mysql table
mysql = spark.read \
            .format("org.apache.spark.sql.cassandra") \
            .options(keyspace="flight_delay") \
            .options(table="mysql") \
            .load() \
            .filter(col("id")>fact_records_max_id)

# extract data from mongodb table
mongodb = spark.read \
            .format("org.apache.spark.sql.cassandra") \
            .options(keyspace="flight_delay") \
            .options(table="mongodb") \
            .load() \
            .filter(col("id")>fact_records_max_id)

# integrate data, rename columns, and change datatype
source = mysql.union(mongodb).select(
    col("id").alias("id"),
    col("actualelapsedtime").cast("bigint").alias("actual_elapsed_time"),
    col("airtime").cast("bigint").alias("air_time"),
    col("arrdel15").cast("bigint").alias("arr_delay_15"),
    col("arrdelay").cast("bigint").alias("arr_delay"),
    col("arrdelayminutes").cast("bigint").alias("arr_delay_minutes"),
    col("arrivaldelaygroups").cast("bigint").alias("arr_delay_groups"),
    col("arrtime").cast("bigint").alias("arr_time"),
    col("arrtimeblk").alias("arr_time_block"),
    col("cancellationcode").alias("cancellation_code"),
    col("cancelled").cast("bigint"),
    col("carrierdelay").cast("bigint").alias("carrier_delay"),
    col("crsarrtime").alias("crs_arr_time"),
    col("crsdeptime").alias("crs_dep_time"),
    col("crselapsedtime").cast("bigint").alias("crs_elapsed_time"),
    col("dayofmonth").alias("day_of_month"),
    col("dayofweek").alias("day_of_week"),
    col("departuredelaygroups").cast("bigint").alias("dep_delay_groups"),
    col("depdel15").cast("bigint").alias("dep_delay_15"),
    col("depdelay").cast("bigint").alias("dep_delay"),
    col("depdelayminutes").cast("bigint").alias("dep_delay_minutes"),
    col("deptime").cast("bigint").alias("dep_time"),
    col("deptimeblk").alias("dep_time_block"),
    col("dest"),
    col("destairportid").alias("dest_airport_id"),
    col("destairportseqid").alias("dest_airport_seq_id"),
    col("destcitymarketid").alias("dest_city_market_id"),
    col("destcityname").alias("dest_city_name"),
    col("deststate").alias("dest_state"),
    col("deststatefips").alias("dest_state_fips"),
    col("deststatename").alias("dest_state_name"),
    col("destwac").alias("dest_wac"),
    col("distance").cast("bigint"),
    col("distancegroup").alias("distance_group"),
    col("diverted").cast("bigint").alias("diverted"),
    col("dot_id_reporting_airline"),
    col("flight_number_reporting_airline"),
    col("flightdate").cast("date").alias("flight_date"),
    col("flights").cast("bigint"),
    col("iata_code_reporting_airline"),
    col("lateaircraftdelay").cast("bigint").alias("late_aircraft_delay"),
    col("month"),
    col("nasdelay").cast("bigint").alias("nas_delay"),
    col("origin"),
    col("originairportid").alias("origin_airport_id"),
    col("originairportseqid").alias("origin_airport_seq_id"),
    col("origincitymarketid").alias("origin_city_market_id"),
    col("origincityname").alias("origin_city_name"),
    col("originstate").alias("origin_state"),
    col("originstatefips").alias("origin_state_fips"),
    col("originstatename").alias("origin_state_name"),
    col("originwac").alias("origin_wac"),
    col("quarter"),
    col("reporting_airline"),
    col("securitydelay").cast("bigint").alias("security_delay"),
    col("tail_number"),
    col("taxiin").cast("bigint").alias("taxi_in"),
    col("taxiout").cast("bigint").alias("taxi_out"),
    col("weatherdelay").cast("bigint").alias("weather_delay"),
    col("wheelsoff").cast("bigint").alias("wheels_on"),
    col("wheelson").cast("bigint").alias("wheels_off"),
    col("year")
)

## define function
# define the function to load data to dim table
def to_dim_table(source_dataframe, table_name, unique_columns, table_columns):
    # get the current table from bigquery
    current_table = spark.read \
                        .format("bigquery") \
                        .options(parentProject="test-373705") \
                        .options(table="flight_delay." + table_name) \
                        .load().select(["id"] + unique_columns)
    
    # get new data from source dataframe
    new_table = source_dataframe.select(table_columns).distinct()
    
    # mapping and fill null id
    dim_table = new_table.join(current_table, on=unique_columns, how="full") \
                        .orderBy(unique_columns) \
                        .withColumn("id", monotonically_increasing_id())
    
    # get max_id of the current table
    max_id = current_table.agg(max("id")).collect()[0][0]

    # ensure max_id has a value
    max_id = -1 if max_id is None else max_id

    # drop old data
    to_append_table = dim_table.filter(col("id")>max_id)

    # append new data to dim table
    to_append_table.orderBy("id") \
               .write \
               .format("bigquery") \
               .options(parentProject="test-373705") \
               .options("flight_delay." + table_name) \
               .option("writeMethod", "direct") \
               .mode("append") \
               .save()

    # return the dim table
    return dim_table

# define function add dim id to source
def add_dim_id(source_dataframe, dim_table, unique_columns, dim_id):
    # return a dataframe added dim id to source
    return source_dataframe.join(dim_table.selectExpr(unique_columns + ["id as " + dim_id]),
                                 on=unique_columns, how="left")

### load data to dim tables
## define arguments
# define dim_date table arguments
unique_date_columns = ["flight_date"]
date_columns = ["year", "quarter", "month", "day_of_month", "day_of_week", "flight_date"]

# define dim_airline table arguments
unique_airline_columns = ["reporting_airline", "tail_number", "flight_number_reporting_airline"]
airline_columns = ["reporting_airline", "dot_id_reporting_airline", "iata_code_reporting_airline",
                   "tail_number", "flight_number_reporting_airline"]

# define dim_origin table arguments
unique_origin_columns = ["origin_airport_id"]
origin_columns = ["origin_airport_id", "origin_airport_seq_id", "origin_city_market_id", "origin",
                  "origin_city_name", "origin_state", "origin_state_fips", "origin_state_name", "origin_wac"]

# define dim_destination table arguments
unique_destination_columns = ["dest_airport_id"]
destination_columns = ["dest_airport_id", "dest_airport_seq_id", "dest_city_market_id", "dest",
                       "dest_city_name", "dest_state", "dest_state_fips", "dest_state_name", "dest_wac"]

# define dim_schedule table arguments
unique_schedule_columns = ["crs_dep_time", "crs_arr_time", "crs_elapsed_time", "distance"]
schedule_columns = ["crs_dep_time", "dep_time_block", "crs_arr_time", "arr_time_block",
                    "crs_elapsed_time", "distance", "distance_group"]

# define dim_cancellations_and_diversions table arguments
unique_cancellations_and_diversions_columns = ["cancelled", "cancellation_code", "diverted"]
cancellations_and_diversions_columns = ["cancelled", "cancellation_code", "diverted"]

## create lists
# create table_name list
table_name_list = ["dim_date", "dim_airline", "dim_origin", "dim_destination",
                   "dim_schedule", "dim_cancellations_and_diversions"]

# create unique_columns list
unique_columns_list = [unique_date_columns, unique_airline_columns, unique_origin_columns, unique_destination_columns,
                       unique_schedule_columns, unique_cancellations_and_diversions_columns]

# create table_columns list
table_columns_list = [date_columns, airline_columns, origin_columns, destination_columns,
                      schedule_columns, cancellations_and_diversions_columns]

# create dim_table list
dim_table_list = []

# create dim_id list
dim_id_list = ["date_id", "airline_id", "origin_id", "destination_id",
               "schedule_id", "cancellations_and_diversions_id"]

# number of dim_table
num_dim_table = len(table_name_list)

## load data
for i in range(num_dim_table):
    # append to list
    dim_table_list.append(to_dim_table(source_dataframe=source, table_name=table_name_list[i],
                                       unique_columns=unique_columns_list[i],
                                       table_columns=table_columns_list[i]))

### load data to fact table
# mappping dim_id
for i in range(num_dim_table):
    # add dim_id
    source = add_dim_id(source_dataframe=source, dim_table=dim_table_list[i],
                        unique_columns=unique_columns_list[i], dim_id=dim_id_list[i])
    
# select necessary columns for fact_records table
fact_records = source.select("id", "date_id", "airline_id", "origin_id", "destination_id", "schedule_id",
                             "cancellations_and_diversions_id", "dep_time", "dep_delay", "dep_delay_minutes",
                             "dep_delay_15", "dep_delay_groups", "taxi_out", "taxi_in", "wheels_off",
                             "wheels_on", "arr_time", "arr_delay", "arr_delay_minutes", "arr_delay_15",
                             "arr_delay_groups", "actual_elapsed_time", "air_time", "flights", "carrier_delay",
                             "weather_delay", "nas_delay", "security_delay","late_aircraft_delay")

# append new data to fact_records table
fact_records.orderBy(col("id").asc()) \
            .write \
            .format("bigquery") \
            .options(parentProject="test-373705") \
            .options(table="flight_delay.fact_records") \
            .option("writeMethod", "direct") \
            .mode("append") \
            .save()

# stop session
spark.stop()
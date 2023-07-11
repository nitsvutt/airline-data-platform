# import libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# create spark session
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
        .config("spark.sql.debug.maxToStringFields", 1000) \
        .getOrCreate()

# get the current max id in cassandra
max_id = spark.read \
        .format("org.apache.spark.sql.cassandra") \
        .options(keyspace="flight_delay", table="mysql") \
        .load().agg(max("id")).collect()[0][0]
# ensure it will be a value
if max_id is None:
    max_id = -1

# read and write by quarter
for i in range(2020,2022):
    for j in range(4):
        # read data filter by quarter
        df = spark.read \
            .format("jdbc") \
            .option("driver","com.mysql.cj.jdbc.Driver") \
            .option("url", "jdbc:mysql://localhost:3306/flight_delay") \
            .option("dbtable", "flight_records") \
            .option("user", "root") \
            .option("password", "admin") \
            .option("numPartitions", 4) \
            .load().filter((col("id")>max_id)&(col("year")==i)&(col("quarter")==j))

        # rename columns
        for column in df.columns:
            df = df.withColumnRenamed(column, column.lower())

        # write data to cassandra
        df.write \
            .format("org.apache.spark.sql.cassandra") \
            .options(keyspace="flight_delay", table="mysql") \
            .mode("append") \
            .save()
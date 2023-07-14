# import libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# create spark session
spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("IngestFromMongoDB") \
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

# read new data to dataframe
data = spark.read \
        .format("mongodb") \
        .option("connection.uri", "mongodb://root:admin@localhost:2717,localhost:2727,localhost:2737/?replicaSet=myReplicaSet") \
        .options(database="flight_delay") \
        .options(collection="flight_records") \
        .load().drop("_id").coalesce(3)

# read and write by quarter
for i in range(2020,2022):
    for j in range(1,13):
        # read data filter by quarter
        df = data.filter((col("year")==i)&(col("month")==j))

        # rename columns
        for column in df.columns:
            df = df.withColumnRenamed(column, column.lower())

        # write data to cassandra
        df.write \
            .format("org.apache.spark.sql.cassandra") \
            .options(keyspace="flight_delay", table="mongodb") \
            .mode("append") \
            .save()

# stop session
spark.stop()
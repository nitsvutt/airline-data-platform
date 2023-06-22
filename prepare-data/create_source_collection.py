# import library
from pymongo import MongoClient

# set up client for mongodb
client = MongoClient("mongodb://root:admin@localhost:2717,localhost:2727,localhost:2737/?replicaSet=myReplicaSet")

# set up db, collections for mongodb
source_collection = client['flight_delay']['flight_records']
target_collection = client['flight_delay']['source']

# fetch the first 1,000,000 documents from the source collection
documents = source_collection.find().limit(1000000)

# insert the documents into the source table
target_collection.insert_many(documents)

# close the database connections
client.close()
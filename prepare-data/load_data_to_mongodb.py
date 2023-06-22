# pip install pymongo

# import libraries
import pandas as pd
import glob
import pymongo

# set up client, db, collection for mongodb
client = pymongo.MongoClient("mongodb://root:admin@localhost:2717,localhost:2727,localhost:2737/?replicaSet=myReplicaSet")
db = client['flight_delay']
collection = db['flight_records']

# get all files from extracted_data/mongodb/db/
mongodb_files = glob.glob("../extracted_data/mongodb/db/*.csv")
mongodb_files.sort()

for file in mongodb_files:
    i = file.split("/")[4].split('.')[0]
    print("Phase " + str(i) + " is running...")
    
    # load csv file to dataframe
    df = pd.read_csv(file)
    
    # convert dataframe to list of dictionaries
    documents = df.to_dict(orient='records')
    
    # load this list to mongodb collection
    collection.insert_many(documents)
    
    print("Phase " + str(i) + " is completed.")

# close the database connections
client.close()
# import libraries
import pandas as pd
import glob
import pymysql
import sqlalchemy

# install pymysql and create mysql engine
pymysql.install_as_MySQLdb()
engine = sqlalchemy.create_engine('mysql://root:admin@localhost:3306/flight_delay')

# get all files from extracted_data/mysql/db/
mysql_files = glob.glob("../extracted_data/mysql/db/*.csv")
mysql_files.sort()

for file in mysql_files:
    i = file.split("/")[4].split('.')[0]
    print("Phase " + str(i) + " is running...")
    
    # load csv file to dataframe
    df = pd.read_csv(file)
    
    # load dataframe to mysql table
    df.to_sql("flight_records", con=engine, if_exists='append', index=False)
    
    print("Phase " + str(i) + " is completed.")
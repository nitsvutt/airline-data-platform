# import libraries
import pandas as pd
import glob
import datetime
import numpy as np

# prepare data for databases
print("Preparing data for databases...")

# get all files from extracted_data/db/
files = glob.glob("../extracted_data/db/*.csv")
files.sort()

for file in files:
    i = file.split("/")[3].split('.')[0]
    print("Phase " + str(i) + " is running...")
    
    # load csv file to dataframe
    df = pd.read_csv("../extracted_data/db/" + str(i) + ".csv")
    df = df.iloc[:, :61]
    df.columns = ['Year', 'Quarter', 'Month', 'DayofMonth', 'DayOfWeek', 'FlightDate',
       'Reporting_Airline', 'DOT_ID_Reporting_Airline',
       'IATA_CODE_Reporting_Airline', 'Tail_Number',
       'Flight_Number_Reporting_Airline', 'OriginAirportID',
       'OriginAirportSeqID', 'OriginCityMarketID', 'Origin', 'OriginCityName',
       'OriginState', 'OriginStateFips', 'OriginStateName', 'OriginWac',
       'DestAirportID', 'DestAirportSeqID', 'DestCityMarketID', 'Dest',
       'DestCityName', 'DestState', 'DestStateFips', 'DestStateName',
       'DestWac', 'CRSDepTime', 'DepTime', 'DepDelay', 'DepDelayMinutes',
       'DepDel15', 'DepartureDelayGroups', 'DepTimeBlk', 'TaxiOut',
       'WheelsOff', 'WheelsOn', 'TaxiIn', 'CRSArrTime', 'ArrTime', 'ArrDelay',
       'ArrDelayMinutes', 'ArrDel15', 'ArrivalDelayGroups', 'ArrTimeBlk',
       'Cancelled', 'CancellationCode', 'Diverted', 'CRSElapsedTime',
       'ActualElapsedTime', 'AirTime', 'Flights', 'Distance', 'DistanceGroup',
       'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay',
       'LateAircraftDelay']
    
    # create index for mongodb and mysql
    idx_mongodb = []
    idx_mysql = []
    for j in df.index.values:
        if j%2==0:
            idx_mongodb.append(j)
        else:
            idx_mysql.append(j)
    
    # initialize mongodb files
    print("Initializing mongodb files...")
    df_mongodb = df.filter(items = idx_mongodb, axis=0)
    df_mongodb.to_csv("../extracted_data/mongodb/db/" + str(i) + ".csv", index=False)
    
    # initialize mysql files
    print("Initializing mysql files...")
    df_mysql = df.filter(items = idx_mysql, axis=0)
    df_mysql.to_csv("../extracted_data/mysql/db/" + str(i) + ".csv", index=False)
    
    print("Phase " + str(i) + " is completed.")
    
print("Data for databases are all prepared.\n")

# prepare data for streaming
print("Preparing data for streaming...")

# get all files from extracted_data/streaming/
files = glob.glob("../extracted_data/streaming/*.csv")
files.sort()

for file in files:
    i = file.split("/")[3].split('.')[0]
    print("Phase " + str(i) + " is running...")
    
    # load csv file to dataframe
    df = pd.read_csv("../extracted_data/streaming/" + str(i) + ".csv")
    df = df.iloc[:, :61]
    df.columns = ['Year', 'Quarter', 'Month', 'DayofMonth', 'DayOfWeek', 'FlightDate',
       'Reporting_Airline', 'DOT_ID_Reporting_Airline',
       'IATA_CODE_Reporting_Airline', 'Tail_Number',
       'Flight_Number_Reporting_Airline', 'OriginAirportID',
       'OriginAirportSeqID', 'OriginCityMarketID', 'Origin', 'OriginCityName',
       'OriginState', 'OriginStateFips', 'OriginStateName', 'OriginWac',
       'DestAirportID', 'DestAirportSeqID', 'DestCityMarketID', 'Dest',
       'DestCityName', 'DestState', 'DestStateFips', 'DestStateName',
       'DestWac', 'CRSDepTime', 'DepTime', 'DepDelay', 'DepDelayMinutes',
       'DepDel15', 'DepartureDelayGroups', 'DepTimeBlk', 'TaxiOut',
       'WheelsOff', 'WheelsOn', 'TaxiIn', 'CRSArrTime', 'ArrTime', 'ArrDelay',
       'ArrDelayMinutes', 'ArrDel15', 'ArrivalDelayGroups', 'ArrTimeBlk',
       'Cancelled', 'CancellationCode', 'Diverted', 'CRSElapsedTime',
       'ActualElapsedTime', 'AirTime', 'Flights', 'Distance', 'DistanceGroup',
       'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay',
       'LateAircraftDelay']
    
    # create index for mongodb and mysql
    idx_mongodb = []
    idx_mysql = []
    for j in df.index.values:
        if j%2==0:
            idx_mongodb.append(j)
        else:
            idx_mysql.append(j)
    
    # initialize mongodb files
    print("Initializing mongodb files...")
    df_mongodb = df.filter(items = idx_mongodb, axis=0)
    df_mongodb.to_csv("../extracted_data/mongodb/streaming/" + str(i) + ".csv", index=False)
    
    # initialize mysql files
    print("Initializing mysql files...")
    df_mysql = df.filter(items = idx_mysql, axis=0)
    df_mysql.to_csv("../extracted_data/mysql/streaming/" + str(i) + ".csv", index=False)
    
    print("Phase " + str(i) + " is completed.")

print("Data for streaming are all prepared.")
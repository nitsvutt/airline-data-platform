# import libraries
import pandas as pd
import glob
import datetime
import numpy as np

# initiate the idex value for the first file
id = 0

# create function to prepare data for specific cases
def prepare_data_for(case):
    # get all files from extracted_data/case/
    files = glob.glob("../extracted_data/" + case + "/*.csv")
    files.sort()

    for file in files:
        i = file.split("/")[3].split('.')[0]
        print("Phase " + str(i) + " is running...")
        
        # load csv file to dataframe
        df = pd.read_csv("../extracted_data/" + case + "/" + str(i) + ".csv")
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
        df['Id'] = df.index + id
        
        # reassign the index value for the next file
        id = df['Id'].max() + 1
        
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
        df_mongodb.to_csv("../extracted_data/mongodb/" + case + "/" + str(i) + ".csv", index=False)
        
        # initialize mysql files
        print("Initializing mysql files...")
        df_mysql = df.filter(items = idx_mysql, axis=0)
        df_mysql.to_csv("../extracted_data/mysql/" + case + "/" + str(i) + ".csv", index=False)
        
        print("Phase " + str(i) + " is completed.")

# prepare data for databases
print("Preparing data for databases...")
prepare_data_for('db')
print("Data for databases are all prepared.\n")

# prepare data for streaming
print("Preparing data for streaming...")
prepare_data_for('streaming')
print("Data for streaming are all prepared.")
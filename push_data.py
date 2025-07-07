import os
import sys
import json
import certifi
import pandas as pd
import pymongo
from dotenv import load_dotenv

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variable
load_dotenv()
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self):
        try:
            logging.info("NetworkDataExtract instance created.")
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_convertor(self, file_path):
        try:
            logging.info(f"Reading CSV from: {file_path}")
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            logging.info(f"Converted {len(records)} records from CSV to JSON.")
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, collection, database):
        try:
            logging.info(f"Connecting to MongoDB database: {database}, collection: {collection}")
            client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = client[database]
            coll = db[collection]

            result = coll.insert_many(records)
            logging.info(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "MehulAI"
    COLLECTION = "NetworkData"

    try:
        networkobj = NetworkDataExtract()
        records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)
        no_of_records = networkobj.insert_data_mongodb(records, COLLECTION, DATABASE)
        print(f"{no_of_records} records inserted successfully.")
    except Exception as e:
        print(f"❌ Error occurred: {e}")
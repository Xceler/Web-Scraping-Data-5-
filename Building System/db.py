from pymongo import MongoClient 
from config import connected_string, db_name, collection_name 

def get_mongo_db():
    try:
        client =MongoClient(connected_string)
        db = client[db_name]
        collection = db[collection_name]
        print("Successfully connected to MongoDB")
        return collection 
    except Exception as e:
        raise ConnectionError("Could Not Connect to MongoDB") from e 
        
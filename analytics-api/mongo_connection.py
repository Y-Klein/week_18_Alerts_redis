import pymongo

def get_mongo_con():
    my_client = pymongo.MongoClient("mongodb://localhost:27017/")
    my_db = my_client["mydatabase"]
    my_col = my_db["customers"]
    return my_col
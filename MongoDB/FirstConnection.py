import pymongo
from pymongo import MongoClient

Con_cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/?retryWrites=true&w=majority")

try :
    db = Con_cluster["ClassTest"]
    collection = db["Users"]
    print("Connection OK")
    data1 = {"animal": "kangaro"}
    collection.update_one({"name":"shalom"},{"$set":{"name":"liroy"}})


except:
    print("Bad Connection")

import gridfs
import pymongo
from pymongo import MongoClient

Con_cluster = MongoClient("mongodb+srv://MongoUser:Password1@clusterdb.ekaau.mongodb.net/?retryWrites=true&w=majority")
db = Con_cluster["ClassTest"]
#collection = db["Users"]
fs = gridfs.GridFS(db)

with open("MongoDB.docx", "rb") as file :
    file_id = fs.put(file, filename="MongoDB.docx")




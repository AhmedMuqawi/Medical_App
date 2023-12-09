from pymongo import MongoClient

mongoDB_url = "mongodb://127.0.0.1:27017/"

client = MongoClient(mongoDB_url)


# Access the database
db = client["MedicalInfoDB"]

import os
from pymongo import MongoClient

# mongoDB_port = os.environ.get(
#     "MONGO_PORT", "27017"
# )  # Get port from environment variable, default to 27017


##for production
# mongoDB_url = "mongodb://mongodb:27017/"
# client = MongoClient(mongoDB_url)


#for develpoing
mongoDB_url = "mongodb://127.0.0.1:27017/"
client = MongoClient(mongoDB_url)

# Access the database
db = client["MedicalInfoDB"]

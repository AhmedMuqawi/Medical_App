import os
from pymongo import MongoClient

# mongoDB_port = os.environ.get(
#     "MONGO_PORT", "27017"
# )  # Get port from environment variable, default to 27017

mongoDB_url = "mongodb://mongodb:27017/"


client = MongoClient(mongoDB_url)

# Access the database
db = client["MedicalInfoDB"]

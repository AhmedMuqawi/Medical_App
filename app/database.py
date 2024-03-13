import os
from pymongo import MongoClient

# mongoDB_port = os.environ.get(
#     "MONGO_PORT", "27017"
# )  # Get port from environment variable, default to 27017


# ##for production
# mongoDB_url = "mongodb://mongodb:27017/"
# client = MongoClient(mongoDB_url)


# ##for develpoing
# mongoDB_url = "mongodb://127.0.0.1:27017/"
# client = MongoClient(mongoDB_url)

##for server
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the MongoDB connection URI from environment variables
MONGODB_URI = os.getenv("MONGODB_URI")

if MONGODB_URI is None:
    raise ValueError("MongoDB connection URI is not set in environment variables.")

# Connect to the MongoDB database
client = MongoClient(MONGODB_URI)

# Access the database
db = client["MedicalInfoDB"]

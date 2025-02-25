from fastapi.testclient import TestClient
from . import database

from .main import app

client = TestClient(app)

db = database.db

excepts = "Photos"

# Get the collection names
collection_names = db.list_collection_names()

# Create a dictionary to store collection names and their document keys
documents_id = {}

# Iterate through collections
for collection_name in collection_names:
    # Get the collection object
    collection = db[collection_name]

    # Get a single document from the collection (assuming at least one document exists)
    sample_document = collection.find_one()

    # Exclude _id field from the document keys
    if sample_document:
        id = [value for value in sample_document.values() if value == "_id"]
        documents_id[collection_name] = id


def test_get_main_category():
    response = client.get("/medical")
    assert response.status_code == 200


def test_get_category():
    response = client.get("/diseases")
    assert response.status_code == 200


def test_get_disease_info():
    for collection in collection_names:
        items = documents_id[collection]
        for item in items:
            response = client.get(f"/{collection}?{item}")
            assert response.status_code == 200



def test_get_Emergency_diseases():
    response = client.get("/Emergency/")
    assert response.status_code == 200


def test_get_Emergency_disease_info():
    items = documents_id["Pediatric Emergency"]
    for item in items:
        response = client.get(f"/Emergency/{item}")
        assert response.status_code == 200

def test_get_random_tip():
    response = client.get("/tip")
    assert response.status_code == 200
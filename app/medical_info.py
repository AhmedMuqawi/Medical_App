import hashlib
from fastapi.responses import JSONResponse
from . import database
from typing import List, Dict
from . import schemas
from bson.objectid import ObjectId
import random

db = database.db


def get_image(image_name: str) -> str:
    photos_collection = db["Photos"]
    image_url = photos_collection.find_one({image_name: {"$exists": True}})
    return image_url.get(image_name)


def get_diseases_types() -> List[schemas.DiseaseCategory]:
    collections_list = db.list_collection_names()
    excepts = ["Photos", "Pediatric Emergency","0-12 months","1-3 years","3-5 years","5-7 years","General","Communication"]
    disease_types_with_images = []

    for collection_name in collections_list:
        if collection_name not in excepts:
            image_url = get_image(collection_name)
            disease_data = schemas.DiseaseCategory(
                disease_type=collection_name, disease_type_image=image_url, diseases=get_diseases_names(collection_name)
            )
            disease_types_with_images.append(disease_data)

    return disease_types_with_images


def get_diseases_names(collection_name: str) -> List[schemas.DiseaseNames]:
    collection = db.get_collection(collection_name)
    documents = list(collection.find({}))
    disease_names_with_images = []
    
    for doc in documents:
        id = list(doc.keys())[0]
        disease_name = list(doc.keys())[1]
        image_url = get_image(disease_name)
        disease_data = schemas.DiseaseNames(
            disease_name=disease_name, disease_image=image_url, ID=str(doc[id])
        )
        disease_names_with_images.append(disease_data)

    return disease_names_with_images


def get_disease_info(collection_name: str, id: str) -> Dict:
    collection = db.get_collection(collection_name)
    try:
        info = collection.find_one({"_id": ObjectId(id)}, projection={"_id": 0})

        key = list(info.keys())[0]
        info = info[key]
        formatted_data = {
            "Symptoms": info["Symptoms"],
            "Red_Flags": info["Red Flags"],
            "Initial_Management": info["Initial management"],
            "Do_Or_Not": info["Do Or Not to Do"],
        }
        return schemas.MedicalInformation(**formatted_data)
    except (ValueError, KeyError, TypeError ) :
        return JSONResponse(status_code=400, content={"Error": "Invalid input data"})
    except AttributeError:
        return JSONResponse(status_code=404, content={"Error": "Disease not found"})
    except ConnectionError:
        return JSONResponse(status_code=503, content={"Error": "Service unavailable"})


def get_advice(collection_name:str,maximum:int) ->Dict:
    num = random.randint(1,maximum)
    collection = db[collection_name]
    query = {str(num): {"$exists": True}}

    # Projection to include only the desired field
    projection = {str(num): 1, "_id": 0}  # Include only the field with the key equal to the random number

    # Find one document and return only the specified field
    advice_field = collection.find_one(query, projection)

    # Extract the value of the field
    field_value = advice_field[str(num)] if advice_field else None

    return field_value


###########################
# book mark
###########################
bookmark_collection = database.db_2["bookmarks"]

def add_string(id:str, string:str):
    # Generate a unique ID for the string based on its hash
    string_id = hashlib.sha256(string.encode()).hexdigest()

    # Update the document with the given ID or insert a new document
    bookmark_collection.update_one(
        {"_id": id},
        {"$addToSet": {"strings": {"id": string_id, "value": string}}},
        upsert=True
    )
    return string_id


def get_strings_by_id(id:str):

    # Find the document with the given ID
    result = bookmark_collection.find_one({"_id": id})

    # If the document exists, return the list of strings, otherwise return an empty list
    if result:
        return result.get("strings", [])
    else:
        return None

def delete_string(id:str, string_id:str):
    result = bookmark_collection.find_one({"_id": id, "strings.id": string_id})
    
    if not result:
        return JSONResponse(status_code=404, content={"Error": "response not found"})

    try:
        # Remove the string with the given ID from the document
        bookmark_collection.update_one(
            {"_id": id},
            {"$pull": {"strings": {"id": string_id}}}
        )
        return JSONResponse(status_code=200, content={"message": "response unbookmarked successfully"})
    except:
        return JSONResponse(status_code=500, content={"Error": "Internal server error"})


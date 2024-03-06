from . import database
from typing import List, Dict
from . import schemas
from bson.objectid import ObjectId

db = database.db


def get_image(image_name: str) -> str:
    photos_collection = db["Photos"]
    image_url = photos_collection.find_one({image_name: {"$exists": True}})
    # if image_url is None:
    #     return "No Photo"
    return image_url.get(image_name)


def get_diseases_types() -> List[schemas.DiseaseCategory]:
    collections_list = db.list_collection_names()
    excepts = ["Photos", "Pediatric Emergency"]
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
        # print(f"id = {doc[id]},disease_name = {disease_name}")
        image_url = get_image(disease_name)
        disease_data = schemas.DiseaseNames(
            disease_name=disease_name, disease_image=image_url, ID=str(doc[id])
        )
        disease_names_with_images.append(disease_data)

    return disease_names_with_images


def get_disease_info(collection_name: str, id: str) -> Dict:
    collection = db.get_collection(collection_name)
    # print(collection)
    info = collection.find_one({"_id": ObjectId(id)}, projection={"_id": 0})
    key = list(info.keys())[0]
    # print(key)
    info = info[key]
    # print(info)
    # print(type(info))
    formatted_data = {
        "Symptoms": info["Symptoms"],
        "Red_Flags": info["Red Flags"],
        "Initial_Management": info["Initial management"],
        "Do_Or_Not": info["Do Or Not to Do"],
    }
    return schemas.MedicalInformation(**formatted_data)
    # return None


# print(get_diseases_types())
# l = get_diseases_types()
# for i in l:
#     print(i)
#     j = get_diseases_names(i)
#     # print(len(j))
#     for k in j:
#         print(k)
#     print("*" * 50)
# print(get_diseases_names("Pediatric Emergency"))
# print(get_disease_info("Miscellaneous", "65e4a4c18bdb9e941ec816a4"))
# print(get_image("Pediatric Emergency"))
# print(len(get_diseases_types()))
# temp = get_diseases_types()
# for i in temp:
#     print(i)

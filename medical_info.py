from . import database
from typing import List, Dict
from . import schemas

db = database.db


def get_image(image_name: str) -> str:
    photos_collection = db["Photos"]
    image_url = photos_collection.find_one({image_name: {"$exists": True}})
    return image_url.get(image_name)


def get_illnesses_types() -> list[str]:
    collections_list = db.list_collection_names()
    return schemas.IllnessCategory(illness_type=collections_list)


def get_illnesses_names(collection_name: str) -> List[str]:
    collection = db.get_collection(collection_name)
    documents = list(collection.find({}, {"_id": 0}))
    all_keys = [key for doc in documents for key in doc.keys()]
    return schemas.IllnessNames(illnesses=all_keys)


def get_illness_info(collection_name: str, document_key: str) -> Dict:
    collection = db[collection_name]
    info = collection.distinct(document_key)[0]
    # print(type(info))
    formatted_data = {
        "Symptoms": info["Symptoms"],
        "Red_Flags": info["Red Flags"],
        "Initial_Management": info["Initial management"],
        "Do_Or_Not": info["Do Or Not to Do"],
    }
    return schemas.MedicalInformation(**formatted_data)


# print(get_illnesses_types())
# l = get_illnesses_types()
# for i in l:
#     print(i)
#     j = get_illnesses_names(i)
#     # print(len(j))
#     for k in j:
#         print(k)
#     print("*" * 50)
# print(get_illnesses_names("Pediatric_Emergency"))
# print(get_illness_info("Urinary_Tract_diseases", "Urinary Tract Infection"))
print(get_image("Pediatric Emergency"))

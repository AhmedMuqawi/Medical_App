from . import database
from typing import List, Dict
from . import schemas

db = database.db
execpts = ["Photos", "Pediatric Emergency"]


def get_image(image_name: str) -> str:
    photos_collection = db["Photos"]
    image_url = photos_collection.find_one({image_name: {"$exists": True}})
    # if image_url is None:
    #     return "No Photo"
    return image_url.get(image_name)


def get_illnesses_types() -> List[schemas.IllnessCategory]:
    collections_list = db.list_collection_names()
    excepts = ["Photos", "Pediatric Emergency"]
    illness_types_with_images = []

    for collection_name in collections_list:
        if collection_name not in excepts:
            image_url = get_image(collection_name)
            illness_data = schemas.IllnessCategory(
                illness_type=collection_name, illness_type_image=image_url
            )
            illness_types_with_images.append(illness_data)

    return illness_types_with_images


def get_illnesses_names(collection_name: str) -> List[schemas.IllnessNames]:
    collection = db.get_collection(collection_name)
    documents = list(collection.find({}, {"_id": 0}))
    illness_names_with_images = []

    for doc in documents:
        for illness_name, _ in doc.items():
            image_url = get_image(illness_name)
            illness_data = schemas.IllnessNames(
                illness_name=illness_name, illness_image=image_url
            )
            illness_names_with_images.append(illness_data)

    return illness_names_with_images


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
# print(get_image("Pediatric Emergency"))
# print(len(get_illnesses_types()))
# temp = get_illnesses_types()
# for i in temp:
#     print(i)

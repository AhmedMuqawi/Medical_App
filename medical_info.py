from database import db
from typing import List, Dict


def get_illnesses_types() -> list[str]:
    collections_list = db.list_collection_names()
    return collections_list


def get_illnesses_names(collection_name: str) -> List[str]:
    collection = db.get_collection(collection_name)
    documents = list(collection.find({}, {"_id": 0}))
    all_keys = [key for doc in documents for key in doc.keys()]
    return all_keys


def get_illness_info(collection_name: str, document_key: str) -> Dict:
    collection = db[collection_name]
    info = collection.distinct(document_key)
    return info


# print(get_illnesses_types())
# l = get_illnesses_types()
# for i in l:
#     print(i)
#     j = get_illnesses_names(i)
#     # print(len(j))
#     for k in j:
#         print(k)
#     print("*" * 50)

# print(get_illness_info("Miscellaneous", "Iron Deficiency anemia"))

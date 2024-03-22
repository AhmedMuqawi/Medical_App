from fastapi import APIRouter
from .. import schemas, medical_info
import random

router = APIRouter()

@router.get("/tip",response_model=schemas.advice,tags=["Tips"])
def get_random_tip():
    collections = {
        "0-12 months":{
            "maximum":20,
            "what_to_say":"Infant Development(0-12 months)"
        },
        "1-3 years":{
            "maximum":10,
            "what_to_say":"Toddler Development(0-12 months)"
        },
        "3-5 years":{
            "maximum":15,
            "what_to_say":"Early Childhood(0-12 months)"
        },
        "5-7 years":{
            "maximum":10,
            "what_to_say":"Perschool Age(0-12 months)"
        },
        "General":{
            "maximum":26,
            "what_to_say":"General Parenting"
        },
        "Communication":{
            "maximum":10,
            "what_to_say":"Communication Skills"
        }
    }
    random_key = random.choice(list(collections.keys()))
    random_value = medical_info.get_advice(random_key,collections[random_key]["maximum"])
    tip = {
        "what_to_say":collections[random_key]["what_to_say"],
        "info":random_value
        }
    return tip
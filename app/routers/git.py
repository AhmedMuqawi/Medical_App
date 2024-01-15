from fastapi import APIRouter
from .. import schemas, medical_info
from typing import List

router = APIRouter(prefix="/GIT", tags=["GIT diseases"])
collection_name = "GIT Diseases"


# get a list of illnesses name
@router.get("/", response_model=List[schemas.IllnessNames])
def read_illnesses():
    illnesses = medical_info.get_illnesses_names(collection_name)
    return illnesses


# get a specific illness information
@router.get("/{illness_name}", response_model=schemas.MedicalInformation)
def read_illness_info(illness_name: str):
    illness_info = medical_info.get_illness_info(collection_name, illness_name)
    return illness_info

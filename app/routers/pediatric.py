from fastapi import APIRouter
from .. import schemas, medical_info
from typing import List


router = APIRouter(prefix="/Emergency", tags=["Pediatric Emergency"])
collection_name = "Pediatric Emergency"


# get a list of diseases name
@router.get("/", response_model=List[schemas.DiseaseNames])
def read_diseases():
    diseases = medical_info.get_diseases_names(collection_name)
    return diseases


# get a specific disease information
@router.get("/{disease_id}", response_model=schemas.MedicalInformation)
def read_disease_info(disease_id: str):
    disease_info = medical_info.get_disease_info(collection_name, disease_id)
    return disease_info

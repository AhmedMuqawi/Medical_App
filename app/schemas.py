from pydantic import BaseModel
from typing import List, Dict, Union


# create pydantic model for the category info
class MedicalCategory(BaseModel):
    medical_category_name: str
    medical_category_image: str


# create pydantic model for the document name
class DiseaseNames(BaseModel):
    disease_name: str
    disease_image: str


# create pydantic model for the collection name and photo
class DiseaseCategory(BaseModel):
    disease_type: str
    disease_type_image: str
    diseases: List[DiseaseNames]


# create pydantic model for the fields
class MedicalInformation(BaseModel):
    Symptoms: List[Union[str, dict]] | str = None
    Red_Flags: List[Union[str, dict]]
    Initial_Management: List[Union[str, dict]]
    Do_Or_Not: Dict[str, List[str]]


# for discussion
# # create pydantic model for symptoms field


# #create pydantic model for red falgs field


# #create pydantic model for initial management field


# #create pydantic model for do and not  field

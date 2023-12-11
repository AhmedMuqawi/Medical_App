from pydantic import BaseModel
from typing import List, Dict, Union


# create pydantic model for the collection name
class IllnessCategory(BaseModel):
    illness_type: str


# create pydantic model for the document name
class IllnessNames(BaseModel):
    illnesses: List[str]


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

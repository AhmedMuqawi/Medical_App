import uvicorn
from os import getenv
from fastapi import FastAPI
from typing import List
from .routers import  pediatric,advice, bookmark
from . import schemas
from . import medical_info
 # for testing

app = FastAPI()


################
# bookmark
################
app.include_router(bookmark.router)
#################
#random_tips
#################
app.include_router(advice.router)
# route that will return the collection name
@app.get("/medical", response_model=List[schemas.MedicalCategory], tags=["Medical"])
def get_main_category():
    emergency = "Pediatric Emergency"
    info = "Medical Information"
    emergency_photo = medical_info.get_image(emergency)
    info_photo = medical_info.get_image(info)
    main_category = [
        {"medical_category_name": emergency, "medical_category_image": emergency_photo},
        {"medical_category_name": info, "medical_category_image": info_photo},
    ]
    return main_category


# route that will return the collection name
@app.get(
    "/diseases", response_model=List[schemas.DiseaseCategory], tags=["Medical Information"]
)
def get_category():
    return medical_info.get_diseases_types()


# include the APIRouters for git, miscellaneous ,etc..
app.include_router(pediatric.router)



@app.get("/{disease_type}", response_model=schemas.MedicalInformation, tags=["diseases information"])
def read_disease_info(disease_type: str,disease_id):
    disease_info = medical_info.get_disease_info(disease_type, disease_id)
    return disease_info



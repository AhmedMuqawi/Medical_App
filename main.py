from fastapi import FastAPI
from .routers import git, miscellaneous, pediatric, respiratory, urinary
from . import schemas
from . import medical_info


app = FastAPI()


# route that will return the collection name
@app.get("/diseases", response_model=schemas.IllnessCategory, tags=["Illness Category"])
def get_category():
    return medical_info.get_illnesses_types()


# include the APIRouters for git, miscellaneous ,etc..
app.include_router(pediatric.router)
app.include_router(git.router)
app.include_router(respiratory.router)
app.include_router(urinary.router)
app.include_router(miscellaneous.router)

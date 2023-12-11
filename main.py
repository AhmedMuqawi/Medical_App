from fastapi import FastAPI
from .routers import git, miscellaneous, pediatric, respiratory, urinary


app = FastAPI()

# include the APIRouters for git, miscellaneous ,etc..
app.include_router(pediatric.router)
app.include_router(git.router)
app.include_router(miscellaneous.router)
app.include_router(respiratory.router)
app.include_router(urinary.router)

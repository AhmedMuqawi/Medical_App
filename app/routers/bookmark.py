from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .. import schemas, medical_info
from typing import List

router = APIRouter(prefix="/Bookmarks", tags=["Bookmarks"])

@router.post("/create/", response_model=schemas.retrieve_bookmark)
async def add_bookmark(bookmark: schemas.create_bookmark):
    string_id = medical_info.add_string(bookmark.user_id, bookmark.chat_response)
    return {"chat_response_id": string_id, "chat_response": bookmark.chat_response}


@router.get("/retrieve/{user_id}/", response_model=List[schemas.retrieve_bookmark])
async def get_bookmarks(user_id: str):
    strings = medical_info.get_strings_by_id(user_id)
    if strings is None:
        return JSONResponse(status_code=404, content={"Error": "Bookmarks not found"})
    return [{"chat_response_id": string["id"], "chat_response": string["value"]} for string in strings]

@router.delete("/delete/{user_id}/{string_id}/", response_model=schemas.retrieve_bookmark)
async def delete_bookmark(user_id: str, string_id: str):
    strings = medical_info.get_strings_by_id(user_id)
    if strings is None:
        return JSONResponse(status_code=404, content={"Error": "Bookmarks not found"})
    medical_info.delete_string(user_id, string_id)
    return {"chat_response_id": string_id, "chat_response": "String deleted successfully"}

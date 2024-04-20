from fastapi import APIRouter

api = APIRouter()


@api.get("/root")
async def root():
    return "example"


@api.get("/error")
async def error():

    return "error"

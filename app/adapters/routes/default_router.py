from fastapi import APIRouter

default_router = APIRouter()

@default_router.get('/')
async def home():
    return {'message': f'Hello, Welcome to the Property API.'}
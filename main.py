from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from mongoengine import connect
from app.adapters.routes.default_router import default_router
from app.adapters.routes.property_router import property_router
from app.adapters.routes.owner_router import owner_router

app = FastAPI(title="FastAPI-Properties-Backend",description = "CRU API")

connect('my_mongodb', host='mongodb://localhost:27017/my_mongodb')

app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers for different entities
app.include_router(default_router)
app.include_router(property_router, prefix="/api")
app.include_router(owner_router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8001)
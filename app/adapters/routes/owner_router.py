from fastapi import APIRouter, HTTPException
from app.core.use_cases.owner_use_cases import OwnerUseCase
from app.adapters.databases.owner_database import MongoDBOwnerRepository
from app.core.models.owner import Owner
from app.adapters.schemas.serializers import owner_serilizer

owner_router = APIRouter()
base = "/owners/"

owner_repository = MongoDBOwnerRepository()
owner_use_case = OwnerUseCase(owner_repository)

@owner_router.get(base+'{id_owner}')
async def get_owner_by_id(id_owner:str)-> Owner:
    owner_entity = owner_use_case.get_owner_by_id(id_owner)
    if owner_entity:
        return owner_entity
    else:
        raise HTTPException(status_code=404, detail="Owner not found")
    
@owner_router.post(base)
async def create_owner(owner:Owner)->Owner:
    new_owner = owner_use_case.create_owner(id_owner=owner.IdOwner, name=owner.Name, address=owner.Address, photo=owner.Photo, birthday=owner.Birthday)
    if new_owner:
        return owner_serilizer(new_owner)
    else:
        raise HTTPException(status_code=404, detail=f"Error creating the owner")

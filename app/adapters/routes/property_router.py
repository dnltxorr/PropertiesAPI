# controllers.py
from fastapi import APIRouter, status, Depends, HTTPException, File, UploadFile
from typing import List
# from adapters.databases.entities.property_entity import PropertyEntity
from app.core.models.property import Property
from app.adapters.schemas.serializers import list_property_serializer, property_serializer, property_image_serializer
from app.utils.utils import getResponse
from app.core.use_cases.property_use_cases import PropertyUseCase
from app.adapters.databases.property_database import MongoDBPropertyRepository
from app.adapters.databases.owner_database import MongoDBOwnerRepository



property_router = APIRouter()

property_repository = MongoDBPropertyRepository()
owner_repository = MongoDBOwnerRepository()
property_use_case = PropertyUseCase(property_repository,owner_repository)

base = '/properties/'
upload_image = f'{base}image-upload/'
update_price = f'{base}update-price/'

@property_router.get(base)
async def get_properties():
    properties_entities = property_use_case.get_properties()
    properties = list_property_serializer(properties_entities)

    return properties

@property_router.get(base+'{id_property}')
async def get_property_by_id(id_property: str) -> Property:
    property_entity = property_use_case.get_property_by_id(id_property)
    if property_entity:
        return property_serializer(property_entity)
    else:
        raise HTTPException(status_code=404, detail="Property not found")
    
@property_router.post(base, response_model=Property)
async def create_property(property:Property) -> Property:
    new_property = property_use_case.create_property(id_property=property.IdProperty,name=property.Name, address=property.Address, price=property.Price, code_internal=property.CodeInternal, year=property.Year, id_owner=property.Owner)
    if new_property:
        return property_serializer(new_property)
    else:
        raise HTTPException(status_code=404, detail="Owner not found")
    
@property_router.post(upload_image)
async def add_property_image(id_property_image:str,id_property:str,enabled: bool,file:UploadFile = File(...)):
    done=await property_use_case.add_property_image(id_property_image=id_property_image,id_property=id_property,file=file, enabled=enabled)
    return getResponse(done, "Property not found")
    
@property_router.put(update_price)
async def update_property_price(id_property: str, new_price: float) -> Property:
    property_entity = property_use_case.update_property_price(id_property, new_price)
    if property_entity:
        return property_serializer(property_entity)
    else:
        raise HTTPException(status_code=404, detail="Property not found")

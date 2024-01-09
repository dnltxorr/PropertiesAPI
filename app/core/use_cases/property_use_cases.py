# use_cases.py
from app.core.repositories.property_repository import PropertyRepository
from app.core.repositories.owner_repository import OwnerRepository
from fastapi import UploadFile
from app.adapters.databases.entities.property_entity import PropertyEntity
from app.adapters.databases.entities.property_image_entity import PropertyImageEntity
from app.adapters.databases.entities.property_trace_entity import PropertyTraceEntity

class PropertyUseCase:
    def __init__(self, property_repository: PropertyRepository, owner_repository: OwnerRepository):
        self.property_repository = property_repository
        self.owner_repository = owner_repository

    def get_properties(self):
        return self.property_repository.get_properties()

    def get_property_by_id(self, id_property: str):
        return self.property_repository.get_property_by_id(id_property)

    def create_property(self, id_property:str, name:str, address: str, price: float, code_internal:str, year:str, id_owner: str):
        owner = self.owner_repository.get_owner_by_id(id_owner)
        if owner:
            new_property = PropertyEntity(IdProperty=id_property,Name=name, Address=address, Price=price, CodeInternal=code_internal, Year=year, Owner=owner)
            return self.property_repository.create_property(new_property)
        return None

    async def add_property_image(self, id_property_image:str,id_property:str,file:UploadFile, enabled: bool):
        return await self.property_repository.add_property_image(PropertyImageEntity(IdPropertyImage=id_property_image,IdProperty=id_property,File="",Enabled=enabled), file=file)

    def update_property_price(self, property_id: str, new_price: float):
        property_entity = self.property_repository.get_property_by_id(property_id)
        if property_entity:
            property_entity.Price = new_price
            return self.property_repository.update_property_price(property_entity)
            
        return None

# repositories.py
from abc import ABC, abstractmethod
from typing import List
from fastapi import UploadFile
from app.adapters.databases.entities.property_entity import PropertyEntity
from app.adapters.databases.entities.property_image_entity import PropertyImageEntity

class PropertyRepository(ABC):
    
    @abstractmethod
    def get_properties(self) -> List[PropertyEntity]:
        pass

    @abstractmethod
    def get_property_by_id(self, id_property:str) -> PropertyEntity:
        pass

    @abstractmethod
    def create_property(self, property_data: PropertyEntity) -> PropertyEntity:
        pass

    @abstractmethod
    async def add_property_image(self, image_data:PropertyImageEntity, file: UploadFile):
        pass

    @abstractmethod
    def update_property_price(self, property_id:str,new_price:float)->PropertyEntity:
        pass

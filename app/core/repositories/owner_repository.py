# repositories.py
from abc import ABC, abstractmethod
from typing import List
from fastapi import UploadFile
from app.adapters.databases.entities.owner_entity import OwnerEntity

class OwnerRepository(ABC):

    @abstractmethod
    def get_owner_by_id(self, id_owner:str) -> OwnerEntity:
        pass

    @abstractmethod
    def create_owner(self,owner_dat:OwnerEntity)->OwnerEntity:
        pass

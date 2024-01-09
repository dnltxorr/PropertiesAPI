# use_cases.py
from app.core.repositories.owner_repository import OwnerRepository
from app.adapters.databases.owner_database import OwnerEntity

class OwnerUseCase:
    def __init__(self, owner_repository: OwnerRepository):
        self.owner_repository = owner_repository

    def create_owner(self, id_owner:str,name: str, address: str, photo: str, birthday: str):
        return self.owner_repository.create_owner(OwnerEntity(IdOwner=id_owner,Name=name, Address=address, Photo=photo, Birthday=birthday))
    
    def get_owner_by_id(self, id_owner: str) -> OwnerEntity:
        return self.owner_repository.get_owner_by_id(id_owner)


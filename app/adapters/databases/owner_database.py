# mongodb_repositories.py
from app.core.repositories.owner_repository import OwnerRepository
from app.adapters.databases.entities.owner_entity import OwnerEntity

class MongoDBOwnerRepository(OwnerRepository):
    
    def get_owner_by_id(self, id_owner: str) -> OwnerEntity:
        return OwnerEntity.objects(IdOwner=id_owner).first()
    
    def create_owner(self, new_owner: OwnerEntity) -> OwnerEntity:
        new_owner.save()
        return new_owner
   
        
    
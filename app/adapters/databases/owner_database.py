# mongodb_repositories.py
from mongoengine import connect
from app.core.repositories.owner_repository import OwnerRepository
from app.adapters.databases.entities.owner_entity import OwnerEntity

# connect('my_mongodb', host='mongodb://localhost:27017/my_mongodb')

class MongoDBOwnerRepository(OwnerRepository):
    
    def get_owner_by_id(self, id_owner: str) -> OwnerEntity:
        return OwnerEntity.objects(IdOwner=id_owner).first()
    
    def create_owner(self, new_owner: OwnerEntity) -> OwnerEntity:
        new_owner.save()
        return new_owner
   
        
    
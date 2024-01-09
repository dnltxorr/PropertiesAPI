# mongodb_repositories.py
from mongoengine import connect
from fastapi import UploadFile
from app.core.repositories.property_repository import PropertyRepository
from app.adapters.databases.entities.property_entity import PropertyEntity
from app.adapters.databases.entities.property_image_entity import PropertyImageEntity
from app.utils.save_picture import save_picture

# connect('my_mongodb', host='mongodb://localhost:27017/my_mongodb')

class MongoDBPropertyRepository(PropertyRepository):

    def get_properties(self):
        return PropertyEntity.objects()
    
    def get_property_by_id(self, id_property: str) -> PropertyEntity:
        return PropertyEntity.objects(IdProperty=id_property).first()
    
    def create_property(self, new_property: PropertyEntity) -> PropertyEntity:
        new_property.save()
        return new_property

    def update_property_price(self, property_entity:PropertyEntity) -> PropertyEntity:
        # property_entity = self.get_property_by_id(property_id)
        if property_entity:
            return property_entity.save()
        return None
    
    async def add_property_image(self, new_image:PropertyImageEntity, file:UploadFile):
        property_entity = self.get_property_by_id(new_image.IdProperty.IdProperty)
        if property_entity:
            imageUrl = save_picture(file=file, folderName='images', fileName=property_entity.Name)
            new_image.File = imageUrl
            if new_image.save():
                return True
            else:
                return False
        else:
            return False
        
    
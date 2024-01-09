from mongoengine import Document, StringField,ReferenceField,BooleanField, CASCADE
from app.adapters.databases.entities.property_entity import PropertyEntity

class PropertyImageEntity(Document):
    IdPropertyImage = StringField(primary_key=True, required=True)
    IdProperty = ReferenceField(PropertyEntity, reverse_delete_rule=CASCADE, db_field='IdProperty')
    File = StringField(required=True)
    Enabled = BooleanField(required=True)
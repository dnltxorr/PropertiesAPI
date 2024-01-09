from mongoengine import Document, StringField, ReferenceField, CASCADE
from app.adapters.databases.entities.property_entity import PropertyEntity

class PropertyTraceEntity(Document):
    IdPropertyTrace = StringField(primary_key=True, required=True)
    DateSale = StringField(required=True)
    Name = StringField(required=True)
    Value = StringField(required=True)
    Tax = StringField(required=True)
    IdProperty = ReferenceField(PropertyEntity, reverse_delete_rule=CASCADE, db_field='IdProperty')
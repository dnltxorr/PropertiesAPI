from mongoengine import Document, StringField, DecimalField, ReferenceField
from app.adapters.databases.entities.owner_entity import OwnerEntity


class PropertyEntity(Document):
    IdProperty = StringField(primary_key=True, required=True)
    Name = StringField(required=True)
    Address = StringField(required=True)
    Price = DecimalField(precision=3, default=0.0,required=True)
    CodeInternal = StringField(required=True)
    Year = StringField(required=True)
    Owner = ReferenceField(OwnerEntity, reverse_delete_rule=None, db_field='IdOwner')
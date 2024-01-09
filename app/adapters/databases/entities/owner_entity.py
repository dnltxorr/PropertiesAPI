from mongoengine import Document, StringField


class OwnerEntity(Document):
    IdOwner = StringField(primary_key=True)
    Name = StringField(required=True)
    Address = StringField(required=True)
    Photo = StringField(required=True)
    Birthday = StringField(required=True)   
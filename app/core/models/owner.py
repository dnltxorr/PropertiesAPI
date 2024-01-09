from pydantic import BaseModel

class Owner(BaseModel):
    IdOwner: str
    Name: str
    Address: str
    Photo: str
    Birthday: str

from pydantic import BaseModel

class PropertyImage(BaseModel):
    IdPropertyImage: str
    IdProperty: str
    File: str
    Enabled: bool
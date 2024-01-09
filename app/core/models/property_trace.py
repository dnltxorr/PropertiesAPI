from pydantic import BaseModel

class PropertyTrace(BaseModel):
    IdPropertyTrace: str
    DateSale: str
    Name: str
    Value: str
    Tax: str
    IdProperty: str
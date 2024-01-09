from pydantic import BaseModel

class Property(BaseModel):
    IdProperty: str
    Name: str
    Address: str
    Price: float
    CodeInternal: str
    Year: str
    Owner: str

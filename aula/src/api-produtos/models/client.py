from pydantic import BaseModel

class Client(BaseModel):
    """
    id, name, age, document, address, phone
    """
    id:int
    name:str
    age:int
    document:str
    address:str
    phone:str
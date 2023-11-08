from pydantic import BaseModel

class Employee(BaseModel):
    """
    name 
    age    
    bithday   
    document     
    address     
    phone     
    salary     
    group    
    function    
    initial_at    
    working 
    gender
    height 
    weight 
    observations
    """

    name:str
    age:int
    bithday:str
    document:str
    address:str
    phone:str
    salary:float
    group:str
    function:str
    initial_at:str
    working:bool
    gender:str
    height:float
    weight:float
    observations:str
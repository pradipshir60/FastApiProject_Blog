from pydantic import BaseModel
from typing import List
    
class Endpointbase(BaseModel):
    name:str
    url:str
    
class Endpoint(Endpointbase):
      class Config():
        orm_mode=True         

class Showendpoint(BaseModel):
    name :str
    url :str
    class Config():
        orm_mode=True                   
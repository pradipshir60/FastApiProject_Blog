from pydantic import BaseModel
from typing import List
    
class Rolebase(BaseModel):
    name:str
    
class Role(Rolebase):
      class Config():
        orm_mode=True         

class Showrole(BaseModel):
    name :str
    class Config():
        orm_mode=True                   
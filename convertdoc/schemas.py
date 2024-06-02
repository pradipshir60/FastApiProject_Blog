from pydantic import BaseModel
from typing import List
    
class Convertdocbase(BaseModel):
    file_name:str
    company:str
    company_address:str
    client_name:str
    
class Convertdoc(Convertdocbase):
      class Config():
        orm_mode=True   
          
class ShowUser(BaseModel):
    first_name:str
    last_name:str
    email:str   
    docs: List[Convertdoc]
    class Config():
        orm_mode=True       

class Showdoc(BaseModel):
    id :int
    file_name :str
    company :str
    company_address:str
    client_name:str
    doccreator:ShowUser
    class Config():
        orm_mode=True                   
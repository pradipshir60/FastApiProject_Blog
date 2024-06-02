from pydantic import BaseModel
from typing import List
    
class Blogbase(BaseModel):
    title:str
    body:str
    
class Blog(Blogbase):
      class Config():
        orm_mode=True   
          
class ShowUser(BaseModel):
    first_name:str
    last_name:str
    email:str   
    blogs: List[Blog]
    class Config():
        orm_mode=True       

class Showblog(BaseModel):
    id :int
    body :str
    title :str
    creator:ShowUser
    class Config():
        orm_mode=True                   
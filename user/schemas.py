from pydantic import BaseModel
from typing import List, Optional
import blog.schemas as schemas    

class User(BaseModel):
    first_name:str
    last_name:str
    email:str
    password:str        

class ShowUser(BaseModel):
    first_name:str
    last_name:str
    email:str   
    blogs: List[schemas.Blog]
    class Config():
        orm_mode=True       

class Login(BaseModel):
    username:   str
    password:   str    
    class Config():
        orm_mode=True  
        
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str]                  
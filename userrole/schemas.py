from pydantic import BaseModel
from typing import List
    
class UserRolebase(BaseModel):
    user_id: int
    role_id: int
    
class UserRole(UserRolebase):
      class Config():   
        orm_mode=True   
          
class ShowUser(BaseModel):
    first_name:str
    last_name:str
    email:str   
    userroles: List[UserRole]
    class Config():
        orm_mode=True  

class ShowRole(BaseModel):
    name:str   
    userroles: List[UserRole]
    class Config():
        orm_mode=True       

class Showuserrole(BaseModel):
    user_id :int
    role_id :int
    users:ShowUser
    roles:ShowRole
    class Config():
        orm_mode=True                   
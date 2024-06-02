from pydantic import BaseModel
from typing import List
    
class MenuRolebase(BaseModel):
    menu_id: int
    role_id: int
    
class MenuRole(MenuRolebase):
      class Config():
        orm_mode=True   
          
class ShowMenu(BaseModel):
    name:str
    url:str
    parent_id: int = None  
    menuroles: List[MenuRole]
    class Config():
        orm_mode=True  

class ShowRole(BaseModel):
    name:str   
    menuroles: List[MenuRole]
    class Config():
        orm_mode=True       

class Showmenurole(BaseModel):
    menu_id :int
    role_id :int
    menus:ShowMenu
    roles:ShowRole
    class Config():
        orm_mode=True                   
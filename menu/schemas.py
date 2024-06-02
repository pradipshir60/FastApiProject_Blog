from pydantic import BaseModel
from typing import List
    
class Menubase(BaseModel):
    name:str
    url:str
    order: int = None
    parent_id: int = None
    
class Menu(Menubase):
    class Config():
        orm_mode=True         

class Showmenu(BaseModel):
    name: str
    url: str
    order: int = None
    parent_id: int = None
    class Config():
        orm_mode=True     

class MenuWithChildren(BaseModel):
    menu: Menu
    children: List[Menu] = []
    class Config:
        orm_mode = True              
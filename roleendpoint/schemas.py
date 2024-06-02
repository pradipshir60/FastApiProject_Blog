from pydantic import BaseModel
from typing import List
    
class RoleEndpointbase(BaseModel):
    endpoint_id:int
    role_id:int
    
class RoleEndpoint(RoleEndpointbase):
      class Config():
        orm_mode=True   
          
class ShowEndpoint(BaseModel):
    name:str
    url:str   
    roleendpoints: List[RoleEndpoint]
    class Config():
        orm_mode=True  

class ShowRole(BaseModel):
    name:str   
    roleendpoints: List[RoleEndpoint]
    class Config():
        orm_mode=True       

class Showroleendpoint(BaseModel):
    endpoint_id :int
    role_id :int
    endpoints:ShowEndpoint
    roles:ShowRole
    class Config():
        orm_mode=True                   
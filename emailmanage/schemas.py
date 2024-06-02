from pydantic import BaseModel
from typing import List
    
class Email(BaseModel):
    subject:str
    body:str
    attachment:str
    emails:str 
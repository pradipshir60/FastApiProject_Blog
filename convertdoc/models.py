from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
import user.models as User

class Convertdoc(Base):
    __tablename__='convertdoc'
    id =Column(Integer,primary_key=True,index=True)
    file_name=Column(String(100)) 
    company=Column(String(100)) 
    company_address=Column(String(100)) 
    client_name=Column(String(100))    
    user_id=Column(Integer, ForeignKey("users.id"))
    doccreator = relationship("User", back_populates="docs")
    
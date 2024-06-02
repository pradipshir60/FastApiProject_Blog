from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import role.models as Role

class Endpoint(Base):
    __tablename__='endpoints'
    id =Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    url=Column(String(100))
    roleendpoints = relationship("RoleEndpoint", back_populates="endpoints")
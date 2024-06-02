from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import userrole.models as UserRole
import menurole.models as MenuRole

class Role(Base):
    __tablename__='roles'
    id =Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    userroles = relationship("UserRole", back_populates="roles")
    roleendpoints = relationship("RoleEndpoint", back_populates="roles")
    menuroles = relationship("MenuRole", back_populates="roles")
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import endpoint.models as Endpoint
import role.models as Role

class RoleEndpoint(Base):
    __tablename__='roleendpoints'
    id =Column(Integer,primary_key=True,index=True,autoincrement=True)
    endpoint_id = Column(Integer, ForeignKey('endpoints.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    endpoints = relationship("Endpoint", back_populates="roleendpoints")
    roles = relationship("Role", back_populates="roleendpoints")
    
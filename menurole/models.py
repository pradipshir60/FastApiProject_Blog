from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import menu.models as Menu
import role.models as Role

class MenuRole(Base):
    __tablename__='menuroles'
    id =Column(Integer,primary_key=True,index=True,autoincrement=True)
    menu_id = Column(Integer, ForeignKey('menus.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    menus = relationship("Menu", back_populates="menuroles")
    roles = relationship("Role", back_populates="menuroles")
    
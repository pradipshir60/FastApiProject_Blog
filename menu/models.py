from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

class Menu(Base):
    __tablename__='menus'
    id =Column(Integer,primary_key=True,index=True,autoincrement=True)
    name=Column(String(100))
    url=Column(String(100))
    order =Column(Integer)
    parent_id = Column(Integer, ForeignKey('menus.id'), default=None)
    parent = relationship("Menu", remote_side=[id])
    children = relationship("Menu")
    menuroles = relationship("MenuRole",back_populates="menus")
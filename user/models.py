from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import blog.models as Blog
import userrole.models as UserRole
import convertdoc.models as Convertdoc
    
class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    first_name=Column(String(50))
    last_name=Column(String(50))
    email=Column(String(50))
    password=Column(String(100))   
    blogs = relationship("Blog",back_populates="creator")
    userroles = relationship("UserRole",back_populates="users")
    docs = relationship("Convertdoc",back_populates="doccreator")
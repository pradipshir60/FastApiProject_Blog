from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from config.database import Base
import user.models as User
import role.models as Role

class UserRole(Base):
    __tablename__='userroles'
    id =Column(Integer,primary_key=True,index=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    role_id = Column(Integer, ForeignKey('roles.id'), primary_key=True)
    users = relationship("User", back_populates="userroles")
    roles = relationship("Role", back_populates="userroles")
    
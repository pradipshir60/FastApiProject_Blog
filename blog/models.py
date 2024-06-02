from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
import user.models as User

class Blog(Base):
    __tablename__='blogs'
    id =Column(Integer,primary_key=True,index=True)
    title=Column(String(100)) 
    body=Column(String(255))
    user_id=Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")
    
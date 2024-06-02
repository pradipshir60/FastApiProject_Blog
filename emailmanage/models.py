from sqlalchemy import Column, Integer, String
from config.database import Base

class Email(Base):
    __tablename__='emails'
    id =Column(Integer,primary_key=True,index=True)
    subject=Column(String(100)) 
    body=Column(String(255))
    attachment=Column(String(255))
    emails=Column(String(255))    
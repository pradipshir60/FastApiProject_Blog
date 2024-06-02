from fastapi import APIRouter,Depends,status,Response
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

from config import database
import role.schemas as schemas
from typing import List
from sqlalchemy.orm import Session
import role.dao as role
from utility import oauth2

router=APIRouter(
    prefix='/role',
    tags=["role"]
)

@router.get("/list/",response_model=Page[schemas.Showrole])
def allroles(db:Session = Depends(database.get_db)):    
    return paginate(role.get_all(db))

@router.post("/create/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Role,db:Session=Depends(database.get_db), current_user=Depends(oauth2.check_access)) :        
    return role.create(request,db)

@router.get("/view/{id}")
def show(id,response: Response,db : Session = Depends(database.get_db), current_user=Depends(oauth2.check_access) ):
   return role.show(id,response,db)        

@router.put("/update/{id}",status_code=202)
def update(id,response: Response,request: schemas.Role, db : Session= Depends(database.get_db), current_user=Depends(oauth2.check_access)):
    return role.update(id,response,request,db)

@router.delete("/delete/{id}",status_code=204)
def destory(id,response: Response,db : Session= Depends(database.get_db), current_user=Depends(oauth2.check_access)):
    return role.destory(id,response,db)

add_pagination(router)
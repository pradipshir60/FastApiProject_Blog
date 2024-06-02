from fastapi import APIRouter,Depends,status,Response
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

from config import database
import userrole.schemas as schemas
from typing import List
from sqlalchemy.orm import Session
import userrole.dao as userrole
from utility import oauth2

router=APIRouter(
    prefix='/userrole',
    tags=["userrole"]
)

@router.get("/list/",response_model=Page[schemas.Showuserrole])
def alluserrole(db:Session = Depends(database.get_db)):    
    return paginate(userrole.get_all(db))

@router.post("/create/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.UserRole,db:Session=Depends(database.get_db), current_user=Depends(oauth2.check_access)) :        
    return userrole.create(request,db)

@router.get("/view/{id}")
def show(id,response: Response,db : Session = Depends(database.get_db), current_user=Depends(oauth2.check_access) ):
   return userrole.show(id,response,db)   

@router.put("/update/{id}",status_code=202)
def update(id,response: Response,request: schemas.UserRole, db : Session= Depends(database.get_db), current_user=Depends(oauth2.check_access)):
    return userrole.update(id,response,request,db)

@router.delete("/delete/{id}",status_code=204)
def destory(id,response: Response,db : Session= Depends(database.get_db), current_user=Depends(oauth2.check_access)):
    return userrole.destory(id,response,db) 

add_pagination(router)
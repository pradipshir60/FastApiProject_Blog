from fastapi import APIRouter,Depends,status,Response
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate

from config import database
import endpoint.schemas as schemas
from typing import List
from sqlalchemy.orm import Session
import endpoint.dao as endpoint
from utility import oauth2


router=APIRouter(
    prefix='/endpoint',
    tags=["endpoint"]
)

@router.get("/list/",response_model=Page[schemas.Showendpoint])
def allendpoints(db:Session = Depends(database.get_db)):    
    return paginate(endpoint.get_all(db))

@router.post("/create/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Endpoint,db:Session=Depends(database.get_db), current_user=Depends(oauth2.check_access)) :        
    return endpoint.create(request,db)

@router.get("/view/{id}")
def show(id,response: Response,db : Session = Depends(database.get_db), current_user=Depends(oauth2.check_access) ):
   return endpoint.show(id,response,db)        

@router.put("/update/{id}",status_code=202)
def update(id,response: Response, request: schemas.Endpoint, db : Session= Depends(database.get_db), current_user=Depends(oauth2.check_access)):
    return endpoint.update(id,response,request,db)

@router.delete("/delete/{id}",status_code=204)
def destory(id,response: Response, db : Session= Depends(database.get_db), current_user=Depends(oauth2.check_access)):
    return endpoint.destory(id,response,db)

add_pagination(router)
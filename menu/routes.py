from fastapi import APIRouter,Depends,status,Response
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from config import database
import menu.schemas as schemas
from typing import List
from sqlalchemy.orm import Session
import menu.dao as menu

router=APIRouter(
    prefix='/menu',
    tags=["menu"]
)

@router.get("/list/",response_model=Page[schemas.Showmenu])
def allmenus(db:Session = Depends(database.get_db)):    
    return paginate(menu.get_all(db))

@router.post("/create/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.Menu,db:Session=Depends(database.get_db)) :        
    return menu.create(request,db)

@router.get("/view/{id}")
def show(id,response: Response,db : Session = Depends(database.get_db)):
   return menu.show(id,response,db)

@router.put("/update/{id}",status_code=202)
def update(id,response: Response, request: schemas.Menu, db : Session= Depends(database.get_db)):
    return menu.update(id,response,request,db)

@router.delete("/delete/{id}",status_code=204)
def destory(id,response: Response, db : Session= Depends(database.get_db)):
    return menu.destory(id,response,db)

add_pagination(router)
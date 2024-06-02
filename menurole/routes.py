from fastapi import APIRouter,Depends,status,Response
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from config import database
import menurole.schemas as schemas
from sqlalchemy.orm import Session
import menurole.dao as menurole

router=APIRouter(
    prefix='/menurole',
    tags=["menurole"]
)

@router.get("/list/",response_model=Page[schemas.Showmenurole])
def allmenurole(db:Session = Depends(database.get_db)):    
    return paginate(menurole.get_all(db))

@router.post("/create/", status_code=status.HTTP_201_CREATED)
def create(request:schemas.MenuRole,db:Session=Depends(database.get_db)) :        
    return menurole.create(request,db)

@router.get("/view/{id}")
def show(id,response: Response,db : Session = Depends(database.get_db)):
   return menurole.show(id,response,db)   

@router.put("/update/{id}",status_code=202)
def update(id,response: Response,request: schemas.MenuRole, db : Session= Depends(database.get_db)):
    return menurole.update(id,response,request,db)

@router.delete("/delete/{id}",status_code=204)
def destory(id,response: Response,db : Session= Depends(database.get_db)):
    return menurole.destory(id,response,db) 

add_pagination(router)
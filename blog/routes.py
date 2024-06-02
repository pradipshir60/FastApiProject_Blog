from fastapi import APIRouter,Depends, Request,status,Response
from fastapi.responses import HTMLResponse
from fastapi_pagination import Page, Params, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate
from config import database
import blog.schemas as schemas
from sqlalchemy.orm import Session
import blog.dao as blog
from utility import oauth2
from fastapi.templating import Jinja2Templates

router=APIRouter(
    prefix='/blog',
    tags=["blog"]
)

templates = Jinja2Templates(directory="blog/templates")

# Start templates

@router.get("/index/",response_model=Page[schemas.Showblog])
def index(request: Request,db:Session = Depends(database.get_db)):    
    params = Params(size=5)
    context = { "request" : request,"data" : paginate(blog.get_all(db),params)}
    return templates.TemplateResponse("index.html", context)

@router.get("/index/{page}",response_model=Page[schemas.Showblog])
def index(request: Request,page,db:Session = Depends(database.get_db)):    
    params = Params(page=page,size=5)
    context = { "request" : request,"data" : paginate(blog.get_all(db),params)}
    return templates.TemplateResponse("index.html", context)

@router.get("/create/",response_class=HTMLResponse)
def index(request: Request):    
    context = { "request" : request}
    return templates.TemplateResponse("create.html", context)

@router.get("/view/{id}",response_class=HTMLResponse)
def show(request: Request,id,response: Response,db : Session = Depends(database.get_db)):
    context = { "request" : request,"data" : blog.show(id,response,db)}
    return templates.TemplateResponse("view.html", context)

@router.get("/edit/{id}",response_class=HTMLResponse)
def show(request: Request,id,response: Response,db : Session = Depends(database.get_db)):
    context = { "request" : request,"data" : blog.show(id,response,db)}
    return templates.TemplateResponse("edit.html", context)

# End Templates

# Start Backend APIS

@router.get("/list/",response_model=Page[schemas.Showblog])
def allblog(db:Session = Depends(database.get_db), current_user=Depends(oauth2.check_access)):    
    return paginate(blog.get_all(db))

@router.post("/store/", status_code=status.HTTP_200_OK)
def create(request:schemas.Blog,db:Session=Depends(database.get_db), current_user=Depends(oauth2.check_access)) :        
    return blog.create(request,db,1)

@router.get("/show/{id}")
def show(id,response: Response,db : Session = Depends(database.get_db), current_user=Depends(oauth2.check_access) ):
   return blog.show(id,response,db)  

@router.put("/update/{id}",status_code=200)
def update(id,request: schemas.Blog,response: Response, db : Session= Depends(database.get_db)):
    return blog.update(id,request,response,db)

@router.delete("/delete/{id}",status_code=200)
def destory(id,response: Response,db : Session= Depends(database.get_db)):
    return blog.destory(id,response,db) 

# End Backend APIS

add_pagination(router)
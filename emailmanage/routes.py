from fastapi import APIRouter,Depends, File, Form, Request, UploadFile,status,Response
from fastapi.responses import HTMLResponse
from config import database
import emailmanage.schemas as schemas
from sqlalchemy.orm import Session
import emailmanage.dao as email
from fastapi.templating import Jinja2Templates

router=APIRouter(
    prefix='/email',
    tags=["email"]
)

templates = Jinja2Templates(directory="emailmanage/templates")

# Start templates

@router.get("/create/",response_class=HTMLResponse)
def index(request: Request):    
    context = { "request" : request}
    return templates.TemplateResponse("create.html", context)

# End Templates

# Start Backend APIS

@router.post("/simple/", status_code=status.HTTP_200_OK)
def simpleMail(attachment: UploadFile = File(default=None), subject: str = Form(), body: str = Form(), emails: str = Form(),db:Session=Depends(database.get_db)) :        
    return email.sendSimpleMail(db,attachment,subject,body,emails)

@router.post("/html/", status_code=status.HTTP_200_OK)
def htmlMail(attachment: UploadFile = File(default=None), subject: str = Form(), body: str = Form(), emails: str = Form(),db:Session=Depends(database.get_db)) :        
    return email.sendHtmlMail(db,attachment,subject,body,emails)

# End Backend APIS

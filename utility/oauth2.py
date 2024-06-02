from fastapi import Depends,HTTPException, status,Request
from config.database import SessionLocal
from utility import token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from userrole.models import UserRole
from roleendpoint.models import RoleEndpoint
from endpoint.models import Endpoint
from user.models import User
import user.dao as dao

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_permission(data: str= Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(data,credentials_exception)

def check_access(request: Request, data: str= Depends(get_permission)):
    if data != None :
        return get_roles_permission(data,request)
    else:
        pass

def get_roles_permission(data,r):
    db = SessionLocal()
    current_url = r.url
    path_segments = str(current_url).split("/")
    user_path = "/".join(path_segments[3:5])
    user_path = "/"+user_path+"/"
    # print(user_path)
    user = db.query(User).filter_by(email = data).first()
    user_id = user.id
    print("user_id",user_id)
    endpoints = get_permissions_by_user_id(db, user_id)
    # print(endpoints)
    i = 0
    for point in endpoints:
        print(point.url)
        if point.url == user_path:
            i = 1
            break
    if i == 1:
        return user_id
    else:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "No access"
        )
    
def get_permissions_by_user_id(db, user_id: int):
    query = db.query(Endpoint).join(RoleEndpoint,RoleEndpoint.endpoint_id == Endpoint.id).join(UserRole, UserRole.role_id == RoleEndpoint.role_id).filter(UserRole.user_id == user_id)
    # Execute the query and return the results as a list of tuples
    results = query.all()
    return results

def getUserId(request: Request, data: str= Depends(get_permission)):
    return data
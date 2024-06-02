from fastapi import APIRouter,Depends,HTTPException,Response
from config import database
import user.models as models
import utility.token as token
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from sqlalchemy.orm import Session
from utility.hashing import Hash
from fastapi.responses import RedirectResponse
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
router=APIRouter( tags=["authentication"])

@router.post("/login")
def login(request:OAuth2PasswordRequestForm= Depends(), db :Session= Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        return "invalid"
        raise HTTPException(status_code=404,
                            details="invalid exception"                 
                            )
        
    if not Hash.verify(user.password , request.password):
        return "incorrect password"
    
    
    access_token = token.create_access_token(data={"sub": user.email},expires_delta = None)
    return {"access_token": access_token, "token_type": "bearer"}
    
    return user 

@router.post('/logout')
def logout(response : Response, data: str= Depends(oauth2_scheme)):
    response = RedirectResponse(url="/login")
    response.delete_cookie("Authorization", domain="localhost")
    return response


# Define a decorator to check if the user has the required role

# def has_role(roles: List[str]):

#     def decorator(func):

#         async def wrapper(*args, **kwargs):

#             user = await get_current_user()

#             if user["role"] not in roles:

#                 raise HTTPException(status_code=403, detail="User does not have required role")

#             return await func(*args, **kwargs)

#         return wrapper

#     return decorator


   
   
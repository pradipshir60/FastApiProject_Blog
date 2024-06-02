from sqlalchemy.orm import Session
import user.models as models
import user.schemas as schemas
from userrole.models import UserRole
from endpoint.models import Endpoint
from roleendpoint.models import RoleEndpoint
from utility.hashing import Hash
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    users=db.query(models.User).order_by(getattr(models.User, 'id').desc())
    return users

def create(request,db:Session):
    new_user=models.User(first_name=request.first_name,last_name=request.last_name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def profile(db:Session, current_user):
    user=db.query(models.User).filter(models.User.email == current_user).first()
    if not user:
        res = {"detail":f"user with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    endpoints = get_permissions_by_user_id(db,user.id)
    return {"user": user, "endpoints": endpoints}

def show(id,db:Session):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        res = {"detail":f"user with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    endpoints = get_permissions_by_user_id(db,id)
    return {"user": user, "endpoints": endpoints}

def destory(id,response, db: Session):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        response.status_code=404
        res = {"detail":f"user with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        try:
            db.query(models.User).filter(models.User.id==id).delete(synchronize_session=False)
            db.commit()
            response.status_code=200
            return {'msg':'deleted'}
        except Exception as e:
            log = Logger.get()
            log.error(str(e))
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE, 
                detail = str(e)
            )

def update(id,response,request:schemas,db:Session):
    user=db.query(models.User).filter(models.User.id == id).first()
    if not user:
        response.status_code=404
        res = {"detail":f"user with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        db.query(models.User).filter(models.User.id==id).update({'first_name':request.first_name,'last_name':request.last_name,'email':request.email,'password':Hash.bcrypt(request.password)})
        db.commit()
        return {'msg':'updated'}

def get_permissions_by_user_id(db, user_id: int):
    query = db.query(Endpoint).join(RoleEndpoint,RoleEndpoint.endpoint_id == Endpoint.id).join(UserRole, UserRole.role_id == RoleEndpoint.role_id).filter(UserRole.user_id == user_id)
    # Execute the query and return the results as a list of tuples
    results = query.all()
    return results
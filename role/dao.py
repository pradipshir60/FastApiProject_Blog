from sqlalchemy.orm import Session
import role.models as models
import role.schemas as schemas
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    roles=db.query(models.Role).order_by(getattr(models.Role, 'id').desc())
    return roles

def create(request:schemas.Role, db:Session):
    new_role=models.Role(name=request.name)  
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

def show(id, response, db:Session):
    role=db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        response.status_code=404
        res = {"detail":f"role with id {id} not found"}
        log = Logger.get()
        log.info(res)
    return role
    
def destory(id,response, db: Session):
    role=db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        response.status_code=404
        res = {"detail":f"role with id {id} not found"}
        log = Logger.get()
        log.info(res)
    else:
        try:
            db.query(models.Role).filter(models.Role.id==id).delete(synchronize_session=False)
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
    role=db.query(models.Role).filter(models.Role.id == id).first()
    if not role:
        response.status_code=404
        res = {"detail":f"role with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        db.query(models.Role).filter(models.Role.id==id).update({'name':request.name})
        db.commit()
        return {'msg':'updated'}
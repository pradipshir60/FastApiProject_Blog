from sqlalchemy.orm import Session
import userrole.models as models
import userrole.schemas as schemas
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    userroles=db.query(models.UserRole).order_by(getattr(models.UserRole, 'id').desc())
    return userroles

def create(request:schemas.UserRole, db:Session):
    new_userrole=models.UserRole(user_id=request.user_id,role_id=request.role_id)    
    db.add(new_userrole)
    db.commit()
    db.refresh(new_userrole)
    return new_userrole

def show(id, response, db:Session):
    userrole=db.query(models.UserRole).filter(models.UserRole.id == id).first()
    if not userrole:
        response.status_code=404
        res = {"detail":f"userrole with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return userrole
    
def destory(id, response, db: Session):
    userrole=db.query(models.UserRole).filter(models.UserRole.id == id).first()
    if not userrole:
        response.status_code=404
        res = {"detail":f"userrole with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        try:
            db.query(models.UserRole).filter(models.UserRole.id==id).delete(synchronize_session=False)
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

def update(id, response, request:schemas,db:Session):
    userrole=db.query(models.UserRole).filter(models.UserRole.id == id).first()
    if not userrole:
        response.status_code=404
        res = {"detail":f"userrole with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        db.query(models.UserRole).filter(models.UserRole.id==id).update({'user_id':request.user_id,'role_id':request.role_id})
        db.commit()
        return {'msg':'updated'}
from sqlalchemy.orm import Session
import menurole.models as models
import menurole.schemas as schemas
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    menuroles=db.query(models.MenuRole).order_by(getattr(models.MenuRole, 'id').desc())
    return menuroles

def create(request:schemas.MenuRole, db:Session):
    new_menurole=models.MenuRole(menu_id=request.menu_id,role_id=request.role_id)    
    db.add(new_menurole)
    db.commit()
    db.refresh(new_menurole)
    return new_menurole

def show(id, response, db:Session):
    menurole=db.query(models.MenuRole).filter(models.MenuRole.id == id).first()
    if not menurole:
        response.status_code=404
        res = {"detail":f"menurole with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return menurole
    
def destory(id, response, db: Session):
    menurole=db.query(models.MenuRole).filter(models.MenuRole.id == id).first()
    if not menurole:
        response.status_code=404
        res = {"detail":f"menurole with id {id} not found"}
        log = Logger.get()
        log.info(res)
    else:
        try:
            db.query(models.MenuRole).filter(models.MenuRole.id==id).delete(synchronize_session=False)
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
    menurole=db.query(models.MenuRole).filter(models.MenuRole.id == id).first()
    if not menurole:
        response.status_code=404
        res = {"detail":f"menurole with id {id} not found"}
        log = Logger.get()
        log.info(res)
    else:
        db.query(models.MenuRole).filter(models.MenuRole.id==id).update({'menu_id':request.menu_id,'role_id':request.role_id})
        db.commit()
        return {'msg':'updated'}
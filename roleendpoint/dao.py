from sqlalchemy.orm import Session
import roleendpoint.models as models
import roleendpoint.schemas as schemas
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    roleendpoints=db.query(models.RoleEndpoint).order_by(getattr(models.RoleEndpoint, 'id').desc())
    return roleendpoints

def create(request:schemas.RoleEndpoint, db:Session):
    new_roleendpoint=models.RoleEndpoint(endpoint_id=request.endpoint_id,role_id=request.role_id)    
    db.add(new_roleendpoint)
    db.commit()
    db.refresh(new_roleendpoint)
    return new_roleendpoint

def show(id, response, db:Session):
    roleendpoint=db.query(models.RoleEndpoint).filter(models.RoleEndpoint.id == id).first()
    if not roleendpoint:
        response.status_code=404
        res = {"detail":f"roleendpoint with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return roleendpoint
    
def destory(id,response, db: Session):
    roleendpoint=db.query(models.RoleEndpoint).filter(models.RoleEndpoint.id == id).first()
    if not roleendpoint:
        response.status_code=404
        res = {"detail":f"roleendpoint with id {id} not found"}
        log = Logger.get()
        log.info(res)
    else:
        try:
            db.query(models.RoleEndpoint).filter(models.RoleEndpoint.id==id).delete(synchronize_session=False)
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
    roleendpoint=db.query(models.RoleEndpoint).filter(models.RoleEndpoint.id == id).first()
    if not roleendpoint:
        response.status_code=404
        res = {"detail":f"roleendpoint with id {id} not found"}
        log = Logger.get()
        log.info(res)
    else:
        db.query(models.RoleEndpoint).filter(models.RoleEndpoint.id==id).update({'endpoint_id':request.endpoint_id,'role_id':request.role_id})
        db.commit()
        return {'msg':'updated'} 
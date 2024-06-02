from sqlalchemy.orm import Session
import convertdoc.models as models
import convertdoc.schemas as schemas
from fastapi import Depends, HTTPException, status
from utility import Logger

def get_all(db:Session):
    doc=db.query(models.Convertdoc).order_by(getattr(models.Convertdoc, 'id').desc())
    return doc

def create(request:schemas.Convertdoc, db:Session, userid):
    new_doc=models.Convertdoc(company=request.company,company_address=request.company_address,user_id=userid)    
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    return new_doc

def show(id, response, db:Session):
    doc=db.query(models.Convertdoc).filter(models.Convertdoc.id == id).first()
    if not doc:
        response.status_code=404
        res = {"detail":f"doc with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return doc
    
def destory(id, response, db: Session):
    doc=db.query(models.Convertdoc).filter(models.Convertdoc.id == id).first()
    if not doc:
        response.status_code=404
        res = {"detail":f"doc with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        try:
            db.query(models.Convertdoc).filter(models.Convertdoc.id==id).delete(synchronize_session=False)
            db.commit()
            response.status_code=200
            return {'msg':'deleted'}
        except Exception as e:
            log = Logger.get()
            log.error(str(e))
            raise HTTPException(
                status_code = status.HTTP_406_NOT_ACCEPTABLE, 
                detail = "Cannot delete or update a parent row."
            )    

def update(id,request:schemas,response,db:Session):
    doc=db.query(models.Convertdoc).filter(models.Convertdoc.id == id).first()
    if not doc:
        response.status_code=404
        res = {"detail":f"doc with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        db.query(models.Convertdoc).filter(models.Convertdoc.id==id).update({'company':request.company,'company_address':request.company_address})
        db.commit()
        return {'msg':'updated'}
from sqlalchemy.orm import Session
import endpoint.models as models
import endpoint.schemas as schemas
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    endpoints=db.query(models.Endpoint).order_by(getattr(models.Endpoint, 'id').desc())
    return endpoints

def create(request:schemas.Endpoint, db:Session):
    new_endpoint=models.Endpoint(name=request.name,url=request.url)  
    db.add(new_endpoint)
    db.commit()
    db.refresh(new_endpoint)
    return new_endpoint

def show(id, response, db:Session):
    endpoint=db.query(models.Endpoint).filter(models.Endpoint.id == id).first()
    if not endpoint:
        response.status_code=404
        res = {"detail":f"endpoint with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return endpoint
    
def destory(id, response, db: Session):
    endpoint=db.query(models.Endpoint).filter(models.Endpoint.id == id).first()
    if not endpoint:
        response.status_code=404
        res = {"detail":f"endpoint with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        try:
            db.query(models.Endpoint).filter(models.Endpoint.id==id).delete(synchronize_session=False)
            db.commit()
            response.status_code=200
            return {'msg':'deleted'}
        except Exception as e:
            log = Logger.get()
            log.error(str(e))
            raise HTTPException(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, 
                detail = str(e)
            )

def update(id, response, request:schemas,db:Session):
    endpoint=db.query(models.Endpoint).filter(models.Endpoint.id == id).first()
    if not endpoint:
        response.status_code=404
        res = {"detail":f"endpoint with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        db.query(models.Endpoint).filter(models.Endpoint.id==id).update({'name':request.name,'url':request.url})
        db.commit()
        return {'msg':'updated'}
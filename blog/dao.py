from sqlalchemy.orm import Session
import blog.models as models
import blog.schemas as schemas
from fastapi import Depends, HTTPException, status
from utility import Logger

def get_all(db:Session):
    blogs=db.query(models.Blog).order_by(getattr(models.Blog, 'id').desc())
    return blogs

def create(request:schemas.Blog, db:Session, userid):
    new_blog=models.Blog(title=request.title,body=request.body,user_id=userid)    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id, response, db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code=404
        res = {"detail":f"blog with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return blog
    
def destory(id, response, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code=404
        res = {"detail":f"blog with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        try:
            db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
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
    blog=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code=404
        res = {"detail":f"blog with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        db.query(models.Blog).filter(models.Blog.id==id).update({'title':request.title,'body':request.body})
        db.commit()
        return {'msg':'updated'}
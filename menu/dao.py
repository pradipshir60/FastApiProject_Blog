from sqlalchemy.orm import Session
import menu.models as models
import menu.schemas as schemas
from fastapi import HTTPException, status
from utility import Logger

def get_all(db:Session):
    menus=db.query(models.Menu).order_by(getattr(models.Menu, 'id').desc())
    return menus

def create(request:schemas.Menu, db:Session):
    if request.parent_id == 0:
        request.parent_id = None
    try:
        new_menu=models.Menu(name=request.name,url=request.url,parent_id=request.parent_id,order=request.order)  
        db.add(new_menu)
        db.commit()
        db.refresh(new_menu)
        return new_menu
    except Exception as e:
            log = Logger.get()
            log.error(str(e))
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                detail = str(e)
            )

def show(id, response, db:Session):
    endmenu=get_menu_with_children(db,id)
    if not endmenu:
        response.status_code=404
        res = {"detail":f"menu with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    return endmenu
    
def destory(id, response, db: Session):
    menu=db.query(models.Menu).filter(models.Menu.id == id).first()
    if not menu:
        response.status_code=404
        res = {"detail":f"menu with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        try:
            db.query(models.Menu).filter(models.Menu.id==id).delete(synchronize_session=False)
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
    menu=db.query(models.Menu).filter(models.Menu.id == id).first()
    if not menu:
        response.status_code=404
        res = {"detail":f"menu with id {id} not found"}
        log = Logger.get()
        log.info(res)
        return res
    else:
        if request.parent_id == 0:
            request.parent_id = None
        try:
            db.query(models.Menu).filter(models.Menu.id==id).update({'name':request.name,'url':request.url,'parent_id':request.parent_id, 'order':request.order})
            db.commit()
            return {'msg':'updated'}
        except Exception as e:
            log = Logger.get()
            log.error(str(e))
            raise HTTPException(
                status_code = status.HTTP_404_NOT_FOUND, 
                detail = str(e)
            )

def get_menu_with_children(db: Session, menu_id: int):
    try:
        menu = db.query(models.Menu).filter(models.Menu.id == menu_id).first()
        children = db.query(models.Menu).filter(models.Menu.parent_id == menu_id).all()
        return schemas.MenuWithChildren(menu=menu, children=children)
    except Exception as e:
        log = Logger.get()
        log.error(str(e))
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, 
            detail = str(e)
        )
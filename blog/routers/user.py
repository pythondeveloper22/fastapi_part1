import bcrypt
# from .. import schemas, database, models
from blog import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status,Response, HTTPException
from blog.hashing import Hash
router = APIRouter(prefix="/user",)
get_db= database.get_db



@router.post("/", response_model=schemas.ShowUser, tags=["Users"])

def create_user(request: schemas.User,db: Session = Depends(get_db)):
        new_user= models.User(name=request.name, email=request.email,password=Hash.bcript(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


@router.get("/{id}", response_model=schemas.ShowUser, tags=["Users"])
def get_user(id: int, db: Session = Depends(get_db)):
    users = db.query(models.User).filter(models.User.id == id).first()
    if not users:
        raise HTTPException(status_code=404, detail=f'user with {id} not available ')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f'blog with {id} not available '}
    return users

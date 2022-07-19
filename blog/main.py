import email
from turtle import title
from unicodedata import name
from venv import create
from xml.parsers.expat import model
from fastapi import FastAPI, Depends, status, Response, HTTPException
from . import models, schemas, hashing
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List
from passlib.context import CryptContext
from .hashing import Hash


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# save data
@app.post("/", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create_blog(request: schemas.Blog,db: Session = Depends(get_db)):
    new_blog = models.Blog(id=request.id,title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# get all data
@app.get("/blog", response_model= List[schemas.Blogblog], tags=["Blogs"])
def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog 
# get data by id 
@app.get("/blog/{id}", response_model=schemas.Blog, tags=["Blogs"])
def get_by_id(response: Response, id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=404, detail=f'blog with {id} not available ')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f'blog with {id} not available '}
    return blog

# delete data by id 
@app.delete("/blogs/{id}", tags=["Blogs"])
def delete_by_id(response: Response, id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Done'


@app.put("/blg/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update(id,request: schemas.BlogBase, db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f'blog with {id} not available ')

    blog.update(request.dict())
    db.commit()
    return 'Updated'


'''
# 1st way how to hash password
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@app.post("/user")

def create_user(request: schemas.User,db: Session = Depends(get_db)):
        # hashpassword
        hashpassword =pwd_context.hash(request.password)
        new_user= models.User(name=request.name, email=request.email,password=hashpassword)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

'''

# 2nd way how to hash password
# @app.post("/user")

# def create_user(request: schemas.User,db: Session = Depends(get_db)):
#         new_user= models.User(name=request.name, email=request.email,password=hashing.Hash.bcript(request.password))
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return new_user


# 3rd way hashing
# from .hashing import Hash
@app.post("/user", response_model=schemas.ShowUser, tags=["Users"])

def create_user(request: schemas.User,db: Session = Depends(get_db)):
        new_user= models.User(name=request.name, email=request.email,password=Hash.bcript(request.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


@app.get("/user/{id}", response_model=schemas.ShowUser, tags=["Users"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f'user with {id} not available ')
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"details": f'blog with {id} not available '}
    return user


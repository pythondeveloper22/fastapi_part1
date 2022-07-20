from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status,Response ,HTTPException
router = APIRouter(tags=["Blogs"])

# we can define tages in APIRouter
get_db= database.get_db


@router.get("/blog", response_model= List[schemas.Blogblog])
# @router.get("/blog", response_model= List[schemas.Blogblog], tags=["Blogs"])

def all(db: Session = Depends(get_db)):
    blog = db.query(models.Blog).all()
    return blog 

@router.put("/blg/{id}", status_code=status.HTTP_202_ACCEPTED)
# @router.put("/blg/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["Blogs"])
def update(id,request: schemas.BlogBase, db: Session = Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404, detail=f'blog with {id} not available ')

    blog.update(request.dict())
    db.commit()
    return 'Updated'


@router.post("/", status_code=status.HTTP_201_CREATED)
# @router.post("/", status_code=status.HTTP_201_CREATED, tags=["Blogs"])
def create_blog(request: schemas.Blog,db: Session = Depends(get_db)):
    # new_blogs = models.Blog(id=request.id,title=request.title, body=request.body)
    new_blogs = models.Blog(id=request.id,title=request.title, body=request.body)

    db.add(new_blogs)
    db.commit()
    db.refresh(new_blogs)
    return new_blogs

@router.delete("/blogs/{id}")
# @router.delete("/blogs/{id}", tags=["Blogs"])
def delete_by_id(response: Response, id, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'Done'




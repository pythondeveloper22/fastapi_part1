from turtle import title
from pydantic import BaseModel
from sqlalchemy import true


class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    id: int
    title: str
    body: str

# this is used to in response that field only in response model
class Blogblog(BaseModel):
    title: str
    # body: str
    class Config():
        orm_mode=True



class User(BaseModel):
    name:str
    email: str
    password: str


class ShowUser(BaseModel):
    name:str
    email: str
    class Config():
        orm_mode=True


class ShowBlog(BaseModel):
    title:str
    body: str
    creator: ShowUser
    class Config():
        orm_mode=True
    
    
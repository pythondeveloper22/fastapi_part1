from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

# @app.get("/")
# def index():
#     return {"hello": "World"}

# query parameter
# type url http://127.0.0.1:8000/index?limit=10
#example 1
# @app.get("/index")
# def index(limit):
#     return {"data": f"{limit} are data available"}


#example 2
# @app.get("/index")
# def index(limit=29, published: bool =False):
#     # return published
#     # get only published blog
#     if published:
#         return {"data": f"{limit} are published index"}
#     else:
#         return {"data": f"{limit} are all  index"}

# example 3
@app.get("/index")
def index(limit, published):
    # return published
    # get only published blog
    if published:
        return {"data": f"{limit} are published index"}
    else:
        return {"data": f"{limit} are all  index"}


@app.get("/home")
def home():
    return {"data":{"hello": "World"}}


# @app.get("/show/1")
# def show():
#     return {"hello": 1}

# dynamic routing
# i takes bydefault string so that convert in int
@app.get("/show/{id}")
def show(id: int):
    return {"hello": id}

# fallowing documentation

@app.get("/")
async def root():
    return {"message": "Hello World"}


# example 1
# predefined values 
class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# example {file_path:path}

@app.get("/fileses/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Worked on Parameters
from fastapi import FastAPI
from typing import Union

app = FastAPI()

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# @app.get("/items/")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip : skip + limit]

# example 2

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

#example 3

# @app.get("/items/{item_id}")
# async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item



# ----Request Body---------------------#

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()
# @app.post("/items/")
# async def create_item(item: Item):
#     print('this is name of item', item.name)
#     return item
# example 2
# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
    # in item.dict() will all item list in dictionay
    #here is item_dict {'name': 'string', 'description': 'string', 'price': 0.0, 'tax': 0.0}
    
    # print('here is item_dict', item_dict)
    # if item.tax:
    #     price_with_tax = item.price + item.tax
    #     item_dict.update({"price_with_tax": price_with_tax})
    #     print('total',item_dict)
    # return item_dict
# example 3

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}


@app.get("/")
async def create_item():
    return "result"
    
    
from fastapi import FastAPI, Query, Path, Body
from typing import Union, List
from enum import Enum
from pydantic import BaseModel

app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#
# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int,
#         item: Item,
#         user: User,
#         importance: int = Body(gt=0),
#         q: Union[str, None] = None,
#         ):
#
#         results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#         if q:
#             results.update({"q" : q})
#         return results


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results

# @app.put("/items/{item_id}")
# async def update_item(
#         *,
#         item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#         q: Union[str, None] = None,
#         item: Union[Item, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# @app.get("/items/{item_id}")
# async def read_items(
#         item_id: int = Path(title="The ID of the item to get"),
#         q: Union[str, None] = Query(default=None, alias="item-query"),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_item(q: str, item_id: int = Path(title="The ID of the item to get")):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_item(
#         *,
#         item_id: int = Path(title="The ID of the item to get", ge=0, le=10000),
#         q: str,
#         size: float = Query(gt=0, lt=10.5),
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/{item_id}")
# async def read_item(*, item_id: int = Path(title="The ID of the item to get", gt=0, le=1000), q: str):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Union[str, None] = None):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#      return results

# @app.get("/items/")
# async def read_items(q: Union[List[str], None] = Query(default=None)):
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/")
# async def read_items(q: List[str] = Query(default=["foo", "bar"])):
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/")
# async def read_items(q: list = Query(default=[])):
#     query_items = {"q": q}
#     return query_items

# @app.get("/items/")
# async def read_items(q: Union[str, None]= Query(default=None,  title="hello")):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(
#         q: Union[str, None] = Query(
#             default=None,
#             title="Query String 입니다.",
#             description="Query String for the items to search in the database that have a good match",
#             min_length=3),
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# @app.get("/items/")
# async def read_items(q: Union[str, None] = Query(
#     default="fixedquery", min_length=3)
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         price_with_tax = item.price * item.tax
#         item_dict.update({"price_with_tax": price_with_tax})
#     return item_dict
#
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: Union[str, None] = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     return {"item_id": item_id, **item.dict()}

# @app.post("/items/")
# async def create_item(item: Item):
#
#     return item

# fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#
#
# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"
#
#
# # skip의 기본값은 0, limit의 기본값은 10
#
# @app.get("/items")
# async def read_item(skip: int = 0, limit: int = 10):
#     return fake_items_db[skip: skip + limit]
#
# # 여러 경로/쿼리 매개변수(필수값이 아님)
# @app.get("/items/{item_id}")
# async def read_item_query(item_id: str, q: Union[str, None] = None, short: bool = False):
#     item = {"item_id": item_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return item
#
# # None이 없다면 필수 매개변수
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item
#
# #필수 매개변수, 기본값이 있는 매개변수, 선택 매개변수
# @app.get("/items/{item_id}")
# async def read_user_item(
#         item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
# ):
#     item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
#     return item
#
# @app.get("/files/{file_path:path}")
# async def read_file(file_path: str):
#     return {"file_path": file_path}
#
#
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}
#
#
# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
#
# @app.get("/hello/{name}")
# async def say_hello(name: str):
#     return {"message": f"Hello {name}"}
#
#
# # 경로 매개변수
# # @app.get("/items/{item_id}")
# # async def read_item(item_id: int):
# #     return {"item_id": item_id}
# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}
#
#
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

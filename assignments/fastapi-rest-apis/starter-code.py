from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Building REST APIs with FastAPI")


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None


items = [
    Item(id=1, name="Book", description="A sample item"),
    Item(id=2, name="Keyboard", description="Another sample item"),
]


@app.get("/")
def read_root():
    return {"message": "FastAPI REST API is running"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items():
    return items


@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")


class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None


@app.post("/items", status_code=201)
def create_item(payload: ItemCreate):
    new_id = max((item.id for item in items), default=0) + 1
    new_item = Item(id=new_id, name=payload.name, description=payload.description)
    items.append(new_item)
    return new_item


# Challenge ideas:
# - Add PUT/PATCH and DELETE endpoints.
# - Add query parameters for filtering items.
# - Return a custom error when the request body is invalid.
from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database import get_db
from models import Item
from schemas import ItemResponse, ItemCreate, ItemUpdate

router = APIRouter(
    tags=["CRUD"],
    responses={404: {"description": "Not found"}},
)

@router.post("/items", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/items/", response_model=List[ItemResponse])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items

@router.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    return db_item

@router.put("/items/{item_id}", response_model=ItemResponse)
def update_data(item_id: int, item: ItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    update_item = item.model_dump(exclude_unset=True)
    for key, value in update_item.items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/items/{item_id}", response_model=ItemResponse)
def delete_data(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"message": "Элемент успешно удалён", "deleted_id": item_id}


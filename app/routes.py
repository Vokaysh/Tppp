```python
from fastapi import APIRouter

from app import models, database

router = APIRouter()

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.post("/items/")
async def create_item(item: models.Item):
    db = database.get_db()
    item_id = db.push(item.dict())
    return {"item_id": item_id}
```
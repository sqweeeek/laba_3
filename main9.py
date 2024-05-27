from typing import Annotated

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None



@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Petya",
                    "description": "A very nice person",
                    "age": 35,
                    
                },
                {
                    "name": "Vasya"
                    
                },
                {
                    "name": "Nastya"
                    
                },
            ],
        ),
    ],
):
    results = {"name1": item_id, "namename": item}
    return results
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from app.fee_calculator import get_delivery_fee
from pydantic import Field

app = FastAPI()


class Item(BaseModel):
    cart_value: int = Field(gt=0)
    delivery_distance: int = Field(gt=0)
    number_of_items: int = Field(gt=0)
    time: datetime


@app.post("/delivery_fee")
async def create_item(item: Item):
    result = get_delivery_fee(
        item.cart_value, item.delivery_distance, item.number_of_items, item.time
    )
    return {"delivery_fee": result}

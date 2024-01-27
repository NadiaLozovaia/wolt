from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from app.fee_calculator import get_delivery_fee

app = FastAPI()


class Item(BaseModel):
    cart_value: int
    delivery_distance: int
    number_of_items: int
    time: datetime


@app.post("/delivery_fee")
async def create_item(item: Item):
    result = get_delivery_fee(
        item.cart_value, item.delivery_distance, item.number_of_items, item.time
    )
    return {"delivery_fee": result}


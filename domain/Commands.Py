from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from allocation.domain.model import Delivery, Shipping


class AddShipping(BaseModel):
    category: str
    cost: float
    regionId: int
    orderId: int
    insurance: float
    date_to_ship: str    


class ShippingCommand(BaseModel):
    shipping: Shipping


class Update_date_to_ship(ShippingCommand):
    date_to_ship: str


class AddDelivery(BaseModel):
    name: str
    post: str
    permission: str
    available:bool
    task : set() = None

class Add_task(DeliveryCommand):
    task = set()
from pydantic import BaseModel,HttpUrl
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4


class AddShipping(BaseModel):
    _id: UUID
    category: str
    cost: float
    regionId: int
    orderId: int
    insurance: float
    date_to_ship: str  


class AddDelivery(BaseModel):
    user: UUID
    name: str
    post: str
    permission: str
    available:bool
    task : set() = None


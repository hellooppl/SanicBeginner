from pydantic import BaseModel, HttpUrl
from .models import Delivery, Shipping


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


class DeliveryCommand(BaseModel):
    delivery: Delivery
class Update_task(DeliveryCommand):
    task = set()
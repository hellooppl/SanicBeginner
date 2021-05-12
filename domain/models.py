from pydantic import BaseModel
from datetime import date
from uuid import UUID

class Shipping(BaseModel):
    _id: UUID
    category: str
    cost: float
    regionId: int
    orderId: int
    insurance: float
    date_to_ship: str    
    is_deleted: bool=False

    class Config:
        title = "Shipping"
        allow_mutations = False
        extra = "Forbid"

def shipping_factory(
    id: UUID,
    category: str,
    cost: float, 
    regionId: int,
    orderId: int,   
    insurance: float,
    date_to_ship: str,
    is_deleted:bool=False,
) -> Shipping : 
    return Shipping(
        id =id,
        category= category,
        cost= cost,
        regionId= regionId,
        orderId=orderId,
        insurance= insurance,
        date_to_shi= date_to_ship,
        is_deleted=is_deleted

    )


class Delivery(BaseModel):
    user: UUID
    name: str
    post: str
    permission: str
    available:bool
    task : set() = None
    is_deleted:bool = False

    class Config:
        title = "Delivery"
        allow_mutations = False
        extra = "Forbid"

    def allocate(self, order:Shipping):
        self.available = False
        self.task.add(order)
    
    def can_deliver(self, order:Shipping) -> bool:
        return self.available

    def remove_shipping(self, order:Shipping):
        if order in self.task:
            self.task.remove(order)
            self.available = True

    def mark_completed(self, order:Shipping):
        if order in self.task:
            self.task.remove(order)
            self.task.order.status = "Completed"



def delivery_factory(
    user: int,
    name: str,
    post: str,
    permission: str,
    available:bool,
    task : set() = None,
    is_deleted :bool = False
) -> Delivery : 
    return Delivery(
    user= user,
    name= name,
    post= post,
    permission= permission,
    available=available,
    task = task,
    is_deleted=is_deleted
    )

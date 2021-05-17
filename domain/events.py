from uuid import UUID
class Event():
    pass


class NotAvailable(Event):
    user:UUID

class ShippingCreated(Event):
    _id: UUID
    category: str
    cost: float
    regionId: int
    orderId: int
    insurance: float
    date_to_ship: str    
    is_deleted: bool=False

class AllocationRequired(Event):
    user:UUID
    task:set()
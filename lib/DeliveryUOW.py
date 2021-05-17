from .AbstractUOW import *
from ..adapters import repository

class DeliveryUnitOfWork(AbstractUOW):

    async def __init__(self) -> None:
        self.shipping = repository.Shippingrepository([])
        self.delivery = repository.Deliveryrepository([])
        self.committed = False
        
    async def __enter__(self) -> DeliveryUnitOfWork:
        self.shipping = repository.ShippingRepository()
        self.delivery = repository.Deliveryrepository()
        return super().__init__()

    async def __exit__(self, *args):
        super.__exit__(*args)
        self.committed= True

    async def _commit(self):
        self.committed=True
        self.publish_events()

    async def rollback(self):
        self.rollback()  


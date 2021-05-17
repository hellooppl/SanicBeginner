from .AbstractUOW import *
from ..adapters import repository

class ShippingUnitOfWork(AbstractUOW):

    async def __init__(self) -> None:
        self.shipping = repository.Shippingrepository([])
        self.committed = False
        
    async def __enter__(self) -> ShippingUnitOfWork:
        self.shipping = repository.ShippingRepository()
        return super().__init__()

    async def __exit__(self, *args):
        super.__exit__(*args)
        self.committed= True

    async def commit(self):
        self.committed=True

    async def rollback(self):
        self.rollback()  
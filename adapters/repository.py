from ..domain.model import Delivery, Shipping


from typing import List, Dict
from uuid import UUID

from randomthings.app import data_product_list, data_batch_list, data_category



class Shippingrepository:
    # Product model add , update and delete operations
    async def get_shipping(self, id_: UUID) -> Shipping:
        shipping = {}
        if id_ in shipping_list[id_]:
            shipping = shipping_list[id_]
        return Shipping.construct(shipping)



    async def add_shipping(self, model: Shipping):
        values = {
            "_id": model._id,
            "category": model.category,
            "cost": model.cost,
            "regionId": model.regionId,
            "orderId": model.orderId,
            "insurance": model.insurance,
            "date_to_ship": model.date_to_ship
        }
        await model.append(values)

    async def update_shipping(self, model: Shipping) -> None:
        values = {
            "id_": model.id_,
            "category": model.category,
            "cost": model.cost,
            "regionId": model.regionId,
            "orderId": model.orderId,
            "insurance": model.insurance,
            "date_to_ship": model.date_to_ship,
        }
        for i in range(len(self) + 1):
            if self[i]["id_"] == values.id_:
                await self[i].update(values)

    async def delete_shipping(self, model: Shipping):
        if self.id_ in model.id_:
            del model.id_


class Deliveryrepository:

    async def get(self, user: UUID) -> Delivery:
        delivery = {}
        if user in delivery_list[id_]:
            batch = delivery_list[user]
        return Delivery.construct(delivery)

    async def add_delivery(self, model: Delivery):
        values = {
            "user":model.user,
            "name": model.name,
            "post": model.post,
            "permission": model.permission,
            "available":model.available,
            "task" : model.task,
        }
        await model.append(values)

    async def update_delivery(self, model: Delivery):
        values = {
            "user":model.user,
            "name": model.name,
            "post": model.post,
            "permission": model.permission,
            "available":model.available,
            "task" : model.task,
        }

        for i in range(len(self) + 1):
            if self[i]["user"] == values.user:
                await self[i].update(values)

    async def delete_delivery(self, model: Delivery):
        if self.user in model.user:
            del model.user
            return "{model.user} is deleted successfully"

from ..domain.model import Delivery, Shipping


from typing import List, Dict
from uuid import UUID

from randomthings.app import data_product_list, data_batch_list, data_category



class Shippingrepository(AbstractRepository):
    # Product model add , update and delete operations
    def get(self, id_: UUID) -> Shipping:
        shipping = {}
        if id_ in shipping_list[id_]:
            shipping = shipping_list[id_]
        return Shipping.construct(shipping)



    def add(self, batch: model.Shipping):
        values = {
            "_id": model._id,
            "category": model.category,
            "cost": model.cost,
            "regionId": model.regionId,
            "orderId": model.orderId,
            "insurance": model.insurance,
            "date_to_ship": model.date_to_ship
        }
    
    def update(self, model: Shipping) -> None:
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
                self[i].update(values)

    def delete_shipping(self, model: Shipping):
        if self.id_ in model.id_:
            del model.id_


class Deliveryrepository:
    def get(self, user: UUID) -> Delivery:
        delivery = {}
        if user in delivery_list[id_]:
            batch = delivery_list[user]
        return Delivery.construct(delivery)

    def add(self, model: Delivery):
        values = {
            "user":model.user,
            "name": model.name,
            "post": model.post,
            "permission": model.permission,
            "available":model.available,
            "task" : model.task,
        }
        model.append(values)

    def update(self, model: Delivery):
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
                self[i].update(values)

    def delete(self, model: Delivery):
        if self.user in model.user:
            del model.user
            return "{model.user} is deleted successfully"

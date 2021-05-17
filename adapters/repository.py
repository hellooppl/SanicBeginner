from ..domain.models import Delivery, Shipping


from typing import List, Dict
from uuid import UUID
from ..storage import shipping_list, delivery_list
from domain import models

class Shippingrepository(AbstractRepository):
    # Product model add , update and delete operations

    def __init__(self) -> None:
        super().__init__()
        
    def get(self, id_: UUID) -> Shipping:
        shipping = {}
        if id_ in shipping_list[id_]:
            shipping = shipping_list[id_]
        return Shipping.construct(shipping)



    def add(self, batch: models.Shipping):
        values = {
            "_id": models._id,
            "category": models.category,
            "cost": models.cost,
            "regionId": models.regionId,
            "orderId": models.orderId,
            "insurance": models.insurance,
            "date_to_ship": models.date_to_ship,
        }
        models.append(values)
        return models._id
    
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


    def delete(self, model: Shipping):
        values = {
            "id_": model.id_,
            "category": model.category,
            "cost": model.cost,
            "regionId": model.regionId,
            "orderId": model.orderId,
            "insurance": model.insurance,
            "date_to_ship": model.date_to_ship,
        }

        for i in range(len(self)+1): 
            if self[i]["id_"] == values.user:
                self[i]["is_deleted"] == False
            return "{user} is deleted successfully"

    


class Deliveryrepository:
    def get(self, user: UUID) -> Delivery:
        delivery = {}
        if user in delivery_list[user]:
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

    def delete(self, model:Shipping):
        values = {
            "id_": model.id_,
            "category": model.category,
            "cost": model.cost,
            "regionId": model.regionId,
            "orderId": model.orderId,
            "insurance": model.insurance,
            "date_to_ship": model.date_to_ship,
        }

        for i in range(len(self)+1): 
            if self[i]["user"] == values.user:
                self[i]["is_deleted"] == False
            return "{user} is deleted successfully"

from __future__ import annotations
from uuid import UUID
from ..domain.model import Shipping

from ..adapters.repository import (
    ShippingRepository,
    Deliveryrepository,
)

from ..service_layer import abstract, handler
from ..domain import command


def add_shipping(validated_data: abstract.AddShipping) -> None:  # call commmand.py
    shipping = handler.add_shipping(cmd)(
        command.AddShipping(
            category=validated_data.category,
            cost=validated_data.cost,
            regionId=validated_data.regionId,
            orderId=validated_data.orderId,
            insurance=validated_data.insurance,
            date_to_ship=validated_data.date_to_ship,
        )
    )  
    shipping = ShippingRepository
    repo.add_batch(shipping)


def update_shipping_date(id_:UUID,validated_data: abstract.UpdateDateToShip) -> None:
    repo= ShippingRepository()
    shipping = repo.get(id_)
    batch = handler.update_shipping(
        command.UpdadteBatchQuantity(
            model=Batch,quantity=validated_data.quatity
        )
    )
    repo.update_batch(batch)


def add_delivery(validated_data: abstract.AddDelivery) -> None:
    delivery = handler.add_delivery()(
        command.AddDelivery(
            user=validated_data.user,
            name=validated_data.name,
            post=validated_data.post,
            permission=validated_data.permission,
            available=validated_data.available,
            task=validated_data.task
        )
    )
    repo = Deliveryrepository
    repo.add_delivery(delivery)
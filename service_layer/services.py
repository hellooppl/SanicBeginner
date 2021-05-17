from __future__ import annotations
from domain import Commands
from uuid import UUID
from ..domain.models import Shipping
from ..lib import DeliveryUOW, ShippingUOW

from ..adapters.repository import ShippingRepository, Deliveryrepository
from ..service_layer import abstract, handlers
from ..domain import command
from domain import models


async def add_shipping(validated_data: abstract.AddShipping) -> None:  # call commmand.py
    uow = ShippingUOW()
    with uow:
        shipping = handlers.add_shipping(
        command.AddShipping(
            category=validated_data.category,
            cost=validated_data.cost,
            regionId=validated_data.regionId,
            orderId=validated_data.orderId,
            insurance=validated_data.insurance,
            date_to_ship=validated_data.date_to_ship,
        )
    )  
        uow.shipping.add(shipping)
        uow.commit()


async def update_shipping_date(id_:UUID,validated_data: abstract.UpdateDateToShip) -> None:
    uow = ShippingUOW
    with uow:
        model = uow.shipping.get(id_)
        shipping = handlers.update_shipping(
        command.UpdadteShQuantity(
            model=model,quantity=validated_data.quatity
        )
    )
        uow.shipping.update(shipping)
        uow.commit()

async def add_delivery(validated_data: abstract.AddDelivery) -> None:
    delivery = handlers.add_delivery()(
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
    repo.add(delivery)


class InvalidDelivery(Exception):
    pass


async def add_shipping_to_delivery(id_:UUID,validated_data:abstract.AddShipping) -> None:
    uow = DeliveryUOW()
    with uow:
        shipping_id = add_shipping(validated_data)
        delivery = uow.delivery.get(id_)
        if delivery is None:
            raise InvalidDelivery(f"Invalid id for delivery agent {id_}")
        delivery = handlers.add_task(
        command.Add_Task(
            model=delivery,task=shipping_id
        )
        )
        uow.delivery.update(delivery)
        uow.commit()

from service_layer.abstract import AddTask
from ..domain.Commands import AddShipping, AddDelivery,Update_date_to_ship,Update_task
from .. import model

HANDLERS = {
    events.NotAvailable: [not_available],
}  
async def add_shipping(cmd: AddShipping) -> model.Shipping:
    return model.shipping_factory(    
        category= cmd.category,
        cost= cmd.cost,
        regionId= cmd.regionId,
        orderId= cmd.orderId,
        insurance= cmd.insurance,
        date_to_ship= cmd.date_to_ship,
    )


async def update_shipping(cmd: Update_date_to_ship) -> model.Shipping:
    if isinstance(cmd,Update_date_to_ship):
        return cmd.shipping.update({
            'date_to_ship':cmd.date_to_ship
        })

async def update_task(cmd:Update_task) -> model.Delivery:
    if isinstance(cmd,Update_task):
        return cmd.shipping.update({
            'task':cmd.task
        })
    


async def add_delivery(cmd: AddDelivery) -> model.Delivery:
    return model.delivery_factory(
        user=cmd.user,
        name=cmd.name,
        post= cmd.post,
        permission=cmd.permission,
        available=cmd.available,
        task =cmd.task,
    )
from ..domain.command import AddShipping, AddDelivery
from .. import model

async def add_shipping(cmd: AddShipping) -> model.Shipping:
    return model.shipping_factory(    
        category= cmd.category,
        cost= cmd.cost,
        regionId= cmd.regionId,
        orderId= cmd.orderId,
        insurance= cmd.insurance,
        date_to_ship= cmd.date_to_ship,
    )


# async def update_shipping(cmd: Update_date_to_ship) -> model.Shipping:
#     if isinstance(cmd,UpdadteBatchQuantity):
#         return cmd.batch.update({
#             'quantity':cmd.quantity
#         })
    


async def add_delivery(cmd: AddDelivery) -> model.Delivery:
    return model.delivery_factory(
        user=cmd.user,
        name=cmd.name,
        post= cmd.post,
        permission=cmd.permission,
        available=cmd.available,
        task =cmd.task,
    )
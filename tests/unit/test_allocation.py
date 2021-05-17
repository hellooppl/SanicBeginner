from ...domain.models import Delivery, Shipping
from ...domain import events

def test_records_out_of_stock_event_if_cannot_allocate():
    agent = Delivery(name='ADDY',post='CRO',permission='ALL', available=True)
    shipping = Shipping(
    category='a',
    cost='50', 
    regionId=5,
    orderId=8,   
    insurance=5.5,
    date_to_ship='2050-8-8',
    )
    agent.add_shipping_to_deliver(agent.id, shipping)

    assert shipping.events[-1] == events.NotAvailable() 



    
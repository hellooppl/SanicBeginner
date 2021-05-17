from . import Delivery
# domain-layer test:
def test_user_aviliability_to_shipment():
    agent = Delivery(
    name='ADDY',
    post='CRO',
    permission='ALL',
    available=True,
    )

    assert agent.available == True
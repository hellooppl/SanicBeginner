from ..domain import events
async def handle(event: events.Event):
    for handler in HANDLERS[type(event)]:
        handler(event)


async def not_available(event: events.NotAvailable):
    print('The delivery agent is not avialable currently')


HANDLERS = {
    events.NotAvailable: [not_available],
}  
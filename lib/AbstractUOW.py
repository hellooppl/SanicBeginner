from ..adapters import repository
import abc
from ..service_layer import messagebus

class AbstractUnitOfWork(abc.ABC):
    batches: repository.AbstractRepository



    # enter and exit is method supported by context manager
    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()
        self.publish_events()

    def publish_events(self):  #(2)
        for delivery in self.delivery.seen:  #(3)
            while delivery.events:
                event = delivery.events.pop(0)
                messagebus.handle(event)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
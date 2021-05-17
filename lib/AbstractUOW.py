from ..adapters import repository
import abc
from ..service_layer import messagebus

class AbstractUnitOfWork(abc.ABC):
    repo: repository.AbstractRepository


    # enter and exit is method supported by context manager
    def __enter__(self) -> AbstractUnitOfWork:
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()
        self.publish_events()

    def publish_events(self):  #(2)
        for single in self.repo.seen:  #(3)
            while single.events:
                event = single.events.pop(0)
                messagebus.handle(event)

    @abc.abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
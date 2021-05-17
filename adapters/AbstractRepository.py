from abc import ABC as abc
from adapters import repository
from domain import models


class AbstractRepository(abc.ABC):

    # seen stores which objects of the model are used during the session seen is set data type 
    # look at the sub class

    def add(self, base: models.BaseModel):
        self._add(base)
        self.seen.add(base)

    def get(self, reference) -> models.BaseModel:
        base=self._get(reference)
        if base:
            self.seen.add(base)
        return base

    def update(self,base:models.BaseModel):
        result = self._update(base)
        if result:
            self.seen.add(result)
        return result
    
    def delete(self,base:models.BaseModel):
        result = self._delete(base)
        if result:
            self.seen.add(result)
        return result

    @abc.abstractmethod
    def _add(self, base:models.BaseModel):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self,reference):
        raise NotImplementedError

    @abc.abstractmethod
    def _update(self, base:models.BaseModel):
        raise NotImplementedError
    
    @abc.abstractmethod
    def _delete(self, reference):
        raise NotImplementedError

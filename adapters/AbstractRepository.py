class AbstractRepository(abc.ABC):

    @abc.abstractmethod 
    def add(self, base: model.BaseModel):
        raise NotImplementedError 

    @abc.abstractmethod
    def get(self, reference) -> model.BaseModel:
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, base:model.BaseModel):
        raise NotImplementedError
    
    @abc.abstractmethod
    def delete(self, reference):
        raise NotImplementedError
class AbstractRepository(abc.ABC):
    @abc.abstractmethod  #(1)
    def add(self, batch: model.BaseModel):
        raise NotImplementedError  #(2)

    @abc.abstractmethod
    def get(self, reference) -> model.BaseModel:
        raise NotImplementedError
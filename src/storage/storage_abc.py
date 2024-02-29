from abc import ABC, abstractmethod

class Storage_ABC(ABC):

    @abstractmethod
    def retrieve(self):
        pass
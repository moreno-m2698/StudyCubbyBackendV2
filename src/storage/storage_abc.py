from abc import ABC, abstractmethod

class Storage_ABC(ABC):

    @abstractmethod
    def retrieve(self):
        pass

    @abstractmethod
    def upload(self, file_name, path):
        pass
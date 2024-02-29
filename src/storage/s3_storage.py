from src.storage.storage_abc import Storage_ABC




class S3_Storage(Storage_ABC):

    def __init__(self):
        pass

    def retrieve(self):
        print('retrieve')
from src.storage import S3_Storage
from fastapi import HTTPException

class Image_Service():

    def __init__(self):

        BUCKET_NAME = 'fed-alpaca'
        self._storage = S3_Storage(BUCKET_NAME)

    async def get_image(self):
        response = self._storage.get_object(file_name = "test.jpg")
        return response
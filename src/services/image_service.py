from storage import S3_Storage

class Image_Service():

    def __init__(self):

        BUCKET_NAME = 'fed-alpaca'
        self._storage = S3_Storage(BUCKET_NAME)

    def get_image(self):
        pass
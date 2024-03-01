from .storage_abc import Storage_ABC
import boto3
from botocore.exceptions import ClientError



class S3_Storage(Storage_ABC):

    def __init__(self, bucket_name: str):
        self._client = boto3.client("s3")
        self._bucket_name = bucket_name

    @property
    def bucket_name(self):
        return self._bucket_name

    def retrieve(self, file_name: str):
        self._client.download_file(self.bucket_name)
        print('retrieve')

    def upload(self, file_name, path):
        self._client.upload_file(path, self._bucket_name, file_name)
        print(f"Successfully uploaded {file_name}")
from .storage_abc import Storage_ABC
import boto3
from botocore.exceptions import ClientError



class S3_Storage(Storage_ABC):

    def __init__(self):
        self.client = boto3.client("s3")

    def retrieve(self):
        print('retrieve')
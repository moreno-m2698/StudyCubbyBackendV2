import boto3
from botocore.exceptions import ClientError



class S3_Storage():

    def __init__(self, bucket_name: str):
        self._client = boto3.client("s3")
        self._bucket_name = bucket_name

    def download(self, file_name: str):
        self._client.download_file(self.bucket_name)
        print('retrieve')

    def upload(self, file_name, path):
        self._client.upload_file(path, self._bucket_name, file_name)
        print(f"Successfully uploaded {file_name}")\
        
    async def get_object(self, file_name):
        response = self._client.get_object(Bucket = self._bucket_name, Key = file_name)
        print(response)
        print(response["Body"].read())
        return response
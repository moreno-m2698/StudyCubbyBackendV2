from src.storage import S3_Storage


def test_s3_storage_inheretance():
    s3 = S3_Storage(bucket_name="fed-alpaca")

    assert isinstance(s3, S3_Storage)
from src.storage import S3_Storage, Storage_ABC


def test_s3_storage_inheretance():
    s3 = S3_Storage()
    assert issubclass(S3_Storage, Storage_ABC) == True
    assert isinstance(s3, Storage_ABC) == True
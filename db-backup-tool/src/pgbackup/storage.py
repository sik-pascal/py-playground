from http import client
from io import IOBase, TextIOBase


def local(in_file: TextIOBase, out_file: TextIOBase):
    out_file.write(in_file.read())
    out_file.close()
    in_file.close()


def s3(client, in_file: IOBase, bucket: str, name: str):
    client.upload_fileobj(in_file, bucket, name)

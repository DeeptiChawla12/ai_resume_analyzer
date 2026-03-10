import os
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv

load_dotenv()


class BlobUploader:

    def __init__(self):

        connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")

        self.container_name = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

        self.blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

    def upload_file(self, file_bytes, filename):

        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name,
            blob=filename
        )

        blob_client.upload_blob(file_bytes, overwrite=True)

        return f"Uploaded {filename} to Azure Blob"
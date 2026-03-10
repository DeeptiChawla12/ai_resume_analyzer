import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    openai_key = os.getenv("AZURE_OPENAI_API_KEY")
    openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    storage_connection = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    container = os.getenv("AZURE_STORAGE_CONTAINER_NAME")

settings = Settings()
from openai import AzureOpenAI
import pymongo
import os

# return an openai client
def get_openai_client():
    api_version = os.environ["OPENAI_API_VERSION"]
    azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"]
    api_key = os.environ["AZURE_OPENAI_API_KEY"]
    
    client = AzureOpenAI(
        api_version=api_version,
        azure_endpoint=azure_endpoint,
        api_key=api_key,
    )

    return client

# return a Mongodb client
def get_db_client():
    username = os.environ["USER"]
    password = os.environ["PASSWORD"]
    
    uri = f"mongodb+srv://{username}:{password}@cluster0.1prhz2s.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = pymongo.MongoClient(uri)
    return client

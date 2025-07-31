import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

DB = os.getenv("DATABASE_NAME")
URI = os.getenv("MONGODB_URI")


_client = None

def get_mongo_client():
    """Obtiene el cliente MongoDB (lazy loading)"""
    global _client
    if _client is None:
        _client = MongoClient(
            URI,
            server_api=ServerApi("1"),
            tls=True,
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=5000  # Timeout más corto
        )
    return _client

def get_collection(col):
    """Obtiene una colección de MongoDB"""
    client = get_mongo_client()
    return client[DB][col]

def test_connection():
    """Función para probar la conexión (solo cuando sea necesario)"""
    try:
        client = get_mongo_client()
        client.admin.command("ping")
        return True
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return False
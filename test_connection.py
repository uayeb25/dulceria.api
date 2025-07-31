import pytest
from utils.mongodb import get_mongo_client, test_connection, get_collection
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_mongodb_connection():
    """Prueba que la conexión a MongoDB funcione correctamente"""
    try:
        # Usar la función test_connection del módulo
        connection_result = test_connection()
        assert connection_result is True, "La conexión a la base de datos falló"
        
        # También probar obtener el cliente
        client = get_mongo_client()
        assert client is not None, "El cliente MongoDB es None"
        
        # Probar obtener una colección
        collection = get_collection("users")
        assert collection is not None, "Error al obtener la colección users"
        
        print(f"✅ Conexión exitosa a MongoDB")
        
    except Exception as e:
        pytest.fail(f"Error en la conexión a MongoDB: {str(e)}")

def test_environment_variables():
    """Prueba que las variables de entorno estén configuradas"""
    mongodb_uri = os.getenv("MONGODB_URI")
    database_name = os.getenv("MONGO_DB_NAME") or os.getenv("DATABASE_NAME")
    
    assert mongodb_uri is not None, "MONGODB_URI no está configurada"
    assert database_name is not None, "MONGO_DB_NAME o DATABASE_NAME no está configurada"
    
    print(f"✅ Variables de entorno configuradas correctamente")
    print(f"   - Database: {database_name}")

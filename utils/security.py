import os
import secrets
import hashlib
import base64
import jwt

from datetime import datetime, timedelta
from fastapi import HTTPException
from dotenv import load_dotenv
from jwt import PyJWTError
from functools import wraps

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

# Función para crear un JWT
def create_jwt_token(
        firstname:str
        , lastname:str
        , email: str
        , active: bool
        , admin: bool
):
    expiration = datetime.utcnow() + timedelta(hours=1)  # El token expira en 1 hora
    token = jwt.encode(
        {
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "active": active,
            "admin": admin,
            "exp": expiration,
            "iat": datetime.utcnow()
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    return token
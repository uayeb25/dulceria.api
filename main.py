import uvicorn
import logging

from fastapi import FastAPI

from controllers.users import create_user, login
from models.users import User
from models.login import Login

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    return {"version": "0.0.0"}

@app.post("/users")
async def create_user_endpoint(user: User) -> User:
    return await create_user(user)

@app.post("/login")
async def login_access(l: Login) -> dict:
    return await login(l)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
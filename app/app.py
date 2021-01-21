from fastapi import Depends, FastAPI
from .v1 import main as v1

app = FastAPI()

app.include_router(v1.router)

@app.get("/")
async def root():
    return {"message": "Hello!"}

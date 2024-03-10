from fastapi import FastAPI
from src.routers import track_router

app = FastAPI()

app.include_router(track_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
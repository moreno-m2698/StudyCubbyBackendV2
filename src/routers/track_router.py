from fastapi import APIRouter

track_router = APIRouter()

@track_router.get("/tracks/")
async def get_tracks():
    return {"tracks": "track endpoint"}
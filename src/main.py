# Built with ingenuity,
# by Jawwad Abbasi (jawwad@kodelle.com)

import settings
import uvicorn

from fastapi import FastAPI, APIRouter, Request
from v1.controller import Ctrl_v1

app = FastAPI(title="Game Scout API")
router = APIRouter(tags=["API v1"], prefix="/api/v1")

####################################
# Supported endpoints for API v1
####################################

@router.get("/Games")
async def GetGames(request: Request):

    params = dict(request.query_params)
    return Ctrl_v1.GetGames(params)

@router.get("/Games/{game_id}")
async def GetGameById(game_id: int):

    return Ctrl_v1.GetGameById(game_id)

@router.post("/Scraper/Steam")
async def ScrapeSteam(request: Request):
    
    request_data = await request.json()
    return Ctrl_v1.ScrapeSteam(request_data)

app.include_router(router)

####################################
# Initiate web server
####################################

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=settings.FASTAPI_PORT, reload=True)
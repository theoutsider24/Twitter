import json

import sentry_sdk
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from twitter.domain.repository.tweet_repository import TweetRepositry
from twitter.interface.settings import Settings
from twitter.interface.websocket import ConnectionManager
from twitter.service import TweetService

tweet_repository = TweetRepositry()
tweet_service = TweetService(tweet_repository)
settings = Settings()

sentry_sdk.init(
    dsn=settings.sentry_dsn,
    traces_sample_rate=1.0,
)

app = FastAPI()

origins = ["http://localhost", "http://localhost:5173", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

manager = ConnectionManager()


class TweetCreateRequest(BaseModel):
    text: str


@app.get("/tweets")
async def get_tweets():
    return tweet_service.get_all_tweets()


@app.post("/tweets")
async def add_tweet(tweet: TweetCreateRequest):
    tweet = tweet_service.create_tweet(tweet.text, "1")
    await manager.broadcast(json.dumps(tweet.as_dict()))
    return tweet


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            _ = await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)

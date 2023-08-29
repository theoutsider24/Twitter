import asyncio

import sentry_sdk
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from redis import asyncio as aioredis
from websockets.exceptions import ConnectionClosedOK

from twitter.interface.settings import Settings
from twitter.interface.websocket.manager import ConnectionManager

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
redis = aioredis.from_url("redis://redis")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    pubsub = redis.pubsub()
    await manager.connect(websocket)
    await pubsub.subscribe("events")
    try:
        while True:
            message = await pubsub.get_message(
                timeout=50, ignore_subscribe_messages=True
            )
            if message and message.get("type") == "message":
                message_data = message.get("data")
                await manager.send_personal_message(message_data.decode(), websocket)
    except (WebSocketDisconnect, ConnectionClosedOK):
        manager.disconnect(websocket)

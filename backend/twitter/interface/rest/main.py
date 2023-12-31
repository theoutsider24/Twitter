import json
from typing import Annotated

import redis
import sentry_sdk
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

from twitter.domain.auth import validate_token
from twitter.domain.repository.tweet_repository import TweetRepositry
from twitter.interface.settings import Settings
from twitter.service import TweetService

tweet_repository = TweetRepositry()
tweet_service = TweetService(tweet_repository)
settings = Settings()

sentry_sdk.init(
    dsn=settings.sentry_dsn,
    traces_sample_rate=1.0,
)

r = redis.Redis(host="redis", port=6379, db=0)

app = FastAPI()

origins = ["http://localhost", "http://localhost:5173", "http://127.0.0.1:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class TweetCreateRequest(BaseModel):
    text: str


@app.get("/tweets")
async def get_tweets():
    return tweet_service.get_all_tweets()


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user_id(token: Annotated[str, Depends(oauth2_scheme)]):
    return validate_token(token).user_id


@app.post("/tweets")
async def add_tweet(
    tweet: TweetCreateRequest,
    current_user_id: Annotated[str, Depends(get_current_user_id)],
):
    tweet = tweet_service.create_tweet(tweet.text, current_user_id)
    r.publish("events", json.dumps(tweet.as_dict()))
    return tweet

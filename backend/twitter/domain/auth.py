from jose import jwt
from pydantic import BaseModel, Field


class AuthException(Exception):
    pass


class TokenData(BaseModel):
    user_id: str = Field(..., alias="https://twitter.com/user_id")


def validate_token(token) -> TokenData:
    try:
        payload = jwt.decode(
            token, key=None, options={"verify_signature": False}, audience="core"
        )
        return TokenData.model_validate(payload)
    except jwt.ExpiredSignatureError as exc:
        raise AuthException("Token has expired") from exc
    except jwt.JWTClaimsError as exc:
        raise AuthException("Token is invalid") from exc

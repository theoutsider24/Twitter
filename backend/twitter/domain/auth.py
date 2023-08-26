from typing import Dict

from jose import jwt


class AuthException(Exception):
    pass


def validate_token(token) -> Dict:
    try:
        payload = jwt.decode(
            token, key=None, options={"verify_signature": False}, audience="core"
        )
        return payload
    except jwt.ExpiredSignatureError as exc:
        raise AuthException("Token has expired") from exc
    except jwt.JWTClaimsError as exc:
        raise AuthException("Token is invalid") from exc

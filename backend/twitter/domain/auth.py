from jose import jwt


def validate_token(token):
    try:
        payload = jwt.decode(
            token, key=None, options={"verify_signature": False}, audience="core"
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token has expired")
    except jwt.JWTClaimsError:
        raise Exception("Token is invalid")
    except Exception:
        raise Exception("Unable to parse authentication token")

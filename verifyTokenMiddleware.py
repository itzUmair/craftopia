from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import jwt
from dotenv import load_dotenv
import os


load_dotenv()

jwtsecret = os.getenv("JWT_SECRET")
app = FastAPI()


async def verifyToken(request: Request, call_next):
    # try:
    #     authorization_header = request.headers.get("Authorization")
    #     if authorization_header is None:
    #         raise HTTPException(status_code=401, detail="Missing JWT token")
    #     token = authorization_header.split(" ")[1]
    #     decoded_token = jwt.decode(token, jwtsecret, algorithms=["HS256"])
    #     request.state.token = decoded_token
    # except jwt.ExpiredSignatureError:
    #     raise HTTPException(status_code=401, detail="Expired JWT token")
    # except (jwt.DecodeError, IndexError):
    #     raise HTTPException(status_code=401, detail="Invalid JWT token")
    # response = await call_next(request)
    # return response
    try:
        # Token verification logic goes here...
        pass
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Expired JWT token")
    except (jwt.DecodeError, IndexError):
        raise HTTPException(status_code=401, detail="Invalid JWT token")

    response = await call_next(request)
    return response

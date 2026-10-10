# Request ----> Middleware ----> [API functionality] ----> Middleware ----> Response

# 1. Requst Logging
# 2. Manipulate request/response
# 3. Token validation ETC
import uvicorn
from fastapi import Depends, FastAPI, Request

from middleware_and_dependency.dependency import Auth, check_token
from middleware_and_dependency.middleware import MyMiddleware

app = FastAPI()


# CLASS BASED MIDDLEWARE
app.add_middleware(MyMiddleware)

auth = Auth()


# FUNCTIONAL MIDDLEWARE
@app.middleware("http")
async def middleware_format(request: Request, call_next):
    req = request
    # request manipulation
    res = await call_next(req)  # trasfer to API route
    # response manipulation
    return res  # Return the response


@app.middleware("http")
async def my_middleware(request: Request, call_next):
    req = request
    print("Working with Request")
    res = await call_next(req)
    print("Working with Response")
    return res


@app.get("/", dependencies=[Depends(check_token), Depends(auth.check_auth())])
async def home():
    return {"message": "hello fastapi"}


# for Development server
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

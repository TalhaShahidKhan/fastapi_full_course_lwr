from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class MyMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):
        req = request
        print("Working with Request from MyMiddleware class")
        res = await call_next(req)
        print("Working with Response from MyMiddleware class")
        return res

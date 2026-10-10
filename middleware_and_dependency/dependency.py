from fastapi import Header, HTTPException, status


# Demo function based dependency for checking token
async def check_token(token: str = Header(...)):
    if token != "abc123":
        raise HTTPException(status_code=401, detail="Invalid Token")


# Demo class based dependency for Auth


class Auth:
    async def check_auth(isAuthenticated: bool = Header(...)):
        if not isAuthenticated:
            raise HTTPException(
                status_code=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED,
                detail="Authentication required",
            )

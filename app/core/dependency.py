from fastapi import HTTPException, Header


async def check_token_header(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code = 400, detail = "Invalid header: X-Token")


async def check_token(token: str):
    if token != "token":
        raise HTTPException(status_code = 400, detail = "No token provided")

from fastapi import HTTPException, Header


async def verify_token(x_token: str = Header(...)):
    if x_token != "secret-token":
        raise HTTPException(status_code = 400, detail = "Invalid header: X-Token")


async def verify_key(x_key: str = Header(...)):
    if x_key != "secret-key":
        raise HTTPException(status_code = 400, detail = "Invalid header: X-Key")

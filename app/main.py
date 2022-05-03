from enum import Enum
from functools import lru_cache
from typing import Optional

import uvicorn
from fastapi import FastAPI
from fastapi.params import Query
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import JSONResponse

import config
from app.routers import users, home, jobs, items, files


@lru_cache()
def get_settings():
    return config.Settings()


app = FastAPI()
app.include_router(users.router)
app.include_router(home.router)
app.include_router(jobs.router)
app.include_router(files.router)
app.include_router(items.router)


class UserNotFoundException(Exception):
    pass


@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content = { "detail": "User not found" }
    )


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host = "localhost",
        port = 8091,
        reload = True
    )

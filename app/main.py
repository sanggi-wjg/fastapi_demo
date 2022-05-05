import time

import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.core.config import get_config


def create_app():
    c = get_config()
    a = FastAPI(
        title = c.title
    )
    return a


app = create_app()


##################################################################################
# Project Env Settings
##################################################################################
# @lru_cache()
# def get_config_settings():
#     return config.Settings()


##################################################################################
# Database
##################################################################################

##################################################################################
# Middlewares
##################################################################################
@app.middleware("http")
async def ad_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response


##################################################################################
# Exceptions
##################################################################################
class UserNotFoundException(Exception):
    pass


@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content = { "detail": "User not found" }
    )


##################################################################################
# Routers
##################################################################################
# app.include_router(home.router)
# app.include_router(file.router)
# app.include_router(item.router)
# app.include_router(job.router)
# app.include_router(user.router)

##################################################################################
# Main
##################################################################################
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host = "localhost",
        port = 8090,
        reload = True
    )

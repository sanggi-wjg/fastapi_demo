import time

import uvicorn

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.api import home, file, item, job, user
from app.core.config import get_config_settings
from app.core.exceptions import UserNotFoundException

# Settings
settings = get_config_settings()


##################################################################################
# Create APP
##################################################################################
def create_app():
    app = FastAPI(
        debug = settings.debug,
        title = settings.app_name,
        description = settings.app_desc,
    )

    # Middlewares
    @app.middleware("http")
    async def ad_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        response.headers["X-Process-Time"] = str(time.time() - start_time)
        return response

    # Exceptions
    @app.exception_handler(UserNotFoundException)
    async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
        return JSONResponse(
            status_code = 404,
            content = { "detail": "User not found" }
        )

    # Routers
    app.include_router(home.router)
    app.include_router(file.router)
    app.include_router(item.router)
    app.include_router(job.router)
    app.include_router(user.router)

    return app


app = create_app()

##################################################################################
# Main
##################################################################################
if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host = settings.host,
        port = settings.port,
        reload = settings.reload
    )

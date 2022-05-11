import time

import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from starlette.requests import Request

from app.api import home, file, item, job, user
from app.core.config import get_config_settings
from app.core.exceptions import UserNotFoundException, DuplicateUserEmailException, CustomException, custom_exception_handler, user_not_found_exception_handler, user_duplicate_email_exception_handler

from app.db import models
from app.db.database import Engine

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

    # Simple way create the database tables. Or you can use Alembic package.
    if settings.debug:
        models.Base.metadata.create_all(bind = Engine)

    # Middlewares (Some of middleware only activated when not debug mode)
    # app.add_middleware(HTTPSRedirectMiddleware) # Any incoming requests to http or ws will be redirected to the secure scheme instead.
    app.add_middleware(GZipMiddleware, minimum_size = settings.gzip_minimum_size)  # Handles GZip responses for any request that includes "gzip" in the Accept-Encoding header.
    app.add_middleware(TrustedHostMiddleware,
                       allowed_hosts = settings.trust_host)  # Enforces that all incoming requests have a correctly set Host header, in order to guard against HTTP Host Header attacks.
    app.add_middleware(CORSMiddleware, allow_origins = settings.cors_origins, allow_credentials = True, allow_methods = ["*"], allow_headers = ["*"])

    @app.middleware("http")
    async def ad_process_time_header(request: Request, call_next):
        start_time = time.time()
        response = await call_next(request)
        response.headers["X-Process-Time"] = str(time.time() - start_time)
        return response

    # Exception Handlers
    app.add_exception_handler(UserNotFoundException, user_not_found_exception_handler)
    app.add_exception_handler(DuplicateUserEmailException, user_duplicate_email_exception_handler)
    app.add_exception_handler(CustomException, custom_exception_handler)

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

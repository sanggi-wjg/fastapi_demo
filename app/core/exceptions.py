from fastapi import HTTPException
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse


class UserException(Exception):
    pass


class DuplicateUserEmailException(UserException):
    __slots__ = ['user_email']

    def __init__(self, user_email):
        self.user_email = user_email


async def user_duplicate_email_exception_handler(request: Request, e: DuplicateUserEmailException):
    return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST,
        content = { "detail": "Duplicate user email" }
    )


class UserNotFoundException(UserException):
    pass


async def user_not_found_exception_handler(request: Request, e: UserNotFoundException):
    return JSONResponse(
        status_code = status.HTTP_404_NOT_FOUND,
        content = { "detail": "User not found" }
    )


###############################################################################################

class AuthException(Exception):
    pass


class NotExistUserEmail(AuthException):

    def __init__(self, user_email):
        self.user_email = user_email


async def not_exist_user_email_handler(request: Request, e: NotExistUserEmail):
    return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST,
        content = { "detail": f"email({e.user_email}) is not exist" }
    )


class BadCredentials(AuthException):

    def __init__(self, user_email):
        self.user_email = user_email


async def bad_credentials_handler(request: Request, e: BadCredentials):
    return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST,
        content = { "detail": "email or password is wrong" }
    )


class JWTBadCredentials(AuthException):
    pass


async def jwt_bad_credentials_handler(request: Request, e: JWTBadCredentials):
    return HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = { "WWW-Authenticate": "Bearer" }
    )


###############################################################################################


class CustomException(Exception):
    __slots__ = ['name']

    def __init__(self, name):
        self.name = name


async def custom_exception_handler(request: Request, e: CustomException):
    return JSONResponse(
        status_code = status.HTTP_418_IM_A_TEAPOT,
        content = { "detail": f"{request.url}: {e.name} exception!" }
    )

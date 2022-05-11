from starlette.requests import Request
from starlette.responses import JSONResponse


class UserException(Exception):
    pass


class DuplicateUserEmailException(UserException):

    def __init__(self, user_email):
        self.user_email = user_email


async def user_duplicate_email_exception_handler(request: Request, e: DuplicateUserEmailException):
    return JSONResponse(
        status_code = 400,
        content = { "detail": "Duplicate user email" }
    )


class UserNotFoundException(UserException):
    pass


async def user_not_found_exception_handler(request: Request, e: UserNotFoundException):
    return JSONResponse(
        status_code = 404,
        content = { "detail": "User not found" }
    )


###############################################################################################

class CustomException(Exception):
    def __init__(self, name):
        self.name = name


async def custom_exception_handler(request: Request, e: CustomException):
    return JSONResponse(
        status_code = 418,
        content = { "detail": f"{request.url}: {e.name} exception!" }
    )

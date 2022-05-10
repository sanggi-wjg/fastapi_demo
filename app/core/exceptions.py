class UserException(Exception):
    pass


class DuplicateUserEmailException(UserException):

    def __init__(self, user_email):
        self.user_email = user_email


class UserNotFoundException(UserException):
    pass

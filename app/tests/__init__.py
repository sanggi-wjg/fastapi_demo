import unittest
from collections import namedtuple

from colorful_print import color
from starlette.testclient import TestClient

from app.main import create_app, settings

test_client = TestClient(
    app = create_app(),
    base_url = "http://localhost",
    root_path = settings.base_dir
)


class MyTestCase(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.print = namedtuple('TestCasePrint', ['debug', 'info', 'warning', 'error'])
        self.print.debug = magenta
        self.print.info = green
        self.print.warning = yellow
        self.print.error = red


def colorful_dispatcher(c: str, *args, **kwargs):
    dispatch = getattr(color, c)
    dispatch(*args, **kwargs)


def red(*args, **kwargs):
    colorful_dispatcher('red', *args, **kwargs)


def yellow(*args, **kwargs):
    colorful_dispatcher('yellow', *args, **kwargs)


def green(*args, **kwargs):
    colorful_dispatcher('green', *args, **kwargs)


def blue(*args, **kwargs):
    colorful_dispatcher('blue', *args, **kwargs)


def magenta(*args, **kwargs):
    colorful_dispatcher('magenta', *args, **kwargs)


def white(*args, **kwargs):
    colorful_dispatcher('white', *args, **kwargs)

from enum import Enum
from typing import Optional

from pydantic import BaseModel


class LoginSNSType(str, Enum):
    Email: str = "email"
    Kakao: str = "kakao"
    Naver: str = "naver"


class Token(BaseModel):
    token_type: str
    access_token: str


class TokenData(Token):
    username: Optional[str] = None

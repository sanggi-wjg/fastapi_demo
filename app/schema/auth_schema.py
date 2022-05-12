from enum import Enum


class LoginSNSType(str, Enum):
    Email: str = "email"
    Kakao: str = "kakao"
    Naver: str = "naver"

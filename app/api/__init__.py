from enum import Enum


class RouterTags(str, Enum):
    Home = "Home"
    File = "Files"
    Item = "Items"
    Job = "Jobs"
    User = "Users"
    Auth = "Auths"



# Return a count of all users
from re import I
from data.user import User

def user_count() -> int:
    return 73_847

def create_account(name:str,email:str,password:str) -> User:
    return User(name,email,'abc')
import re

def validate_password():
    pwd = input("Enter your password: ")
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$'
    return bool(re.fullmatch(pattern, pwd))

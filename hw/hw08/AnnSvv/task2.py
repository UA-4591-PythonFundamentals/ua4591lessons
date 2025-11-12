password = input("Enter your password: ")

import re

def valid_password(password):
    """ Validates a password"""
    if len(password)<6:
        return False, print("Password must be at least 6 characters.")
    elif len(password)>16:
        return False, print("Password must not be more than 16 characters.") 
    elif not re.search(r"[a-z]", password):
        return False, print("Password must contain at least 1 letter between [a-z].")
    elif not re.search (r"[A-Z]", password):
        return False, print("Password must contain at least 1 letter between [A-Z].")
    elif not re.search(r"[0-9]", password):
        return False, print("Password must contain at least 1 number between [0-9].")
    elif not re.search(r"[$#@]", password):
        return False, print("Password must contain at least 1 character from [$#@].")
    else:
        print("Your password is valid.")


valid_password(password)
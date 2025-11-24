from custom_logger import logging

class UserError(Exception):
    """Base class for user-related exceptions."""
    def __init__(self, message):
        # super().__init__(message)
        logging.error(message)

class User:
    def __init__(self, username, age):
        if type(username) is not str:
            raise UserError("Username must be a string.")
        self.username = username
        if type(age) is not int:
            raise UserError("Age must be a non-negative integer.")
        self.age = age
        logging.info(f"User created: {self.username}, Age: {self.age}")

    def validate(self): 
        if not self.username.isalpha():
            raise UserError("Username must contain only alphabetic characters.")
        if self.age < 0 or self.age > 120:
            raise UserError("Age must be between 0 and 120.")
        logging.debug(f"User validated: {self.username}, Age: {self.age}")
        return True

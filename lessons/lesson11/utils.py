from user import User
from custom_logger import logging

def generate_users(user_data):
    logging.info("Starting user generation.")
    users = []
    for username, age in user_data:
        try:
            user = User(username, age)
            user.validate()
            users.append(user)
        except Exception as e:
            logging.error(f"Failed to create/validate user ({username}, {age}): {e}")
    logging.info("User generation complete.")
    return users
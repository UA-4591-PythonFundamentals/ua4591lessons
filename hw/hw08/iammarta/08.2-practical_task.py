import re

password = input("Enter your password: ")

pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@]).{6,16}$'

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")

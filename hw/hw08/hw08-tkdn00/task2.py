import re
password = input("Enter your password: ")
pattern = re.compile('^(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[$#@]).{6,16}$')

if pattern.match(password):
    print("Password match")
else:
    print("Password not match")
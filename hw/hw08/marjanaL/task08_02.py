import re
p = input("Enter your password: ")
pattern = r'[a-z]+[A-Z]+[0-9]+[@#$]+'
if 6 <= len(p) <= 16 and re.match(pattern, p):
    print("Your password is valid")
else:
    print("Your password is invalid")

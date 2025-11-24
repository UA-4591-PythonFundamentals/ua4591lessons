import re

def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"
    
    if re.match(pattern, password):
        return True
    else:
        return False

if __name__ == "__main__":
    password_input = input("Enter your password to check: ")
    
    if validate_password(password_input):
        print("\nPassword is Valid!")
    else:
        print("\nPassword is Invalid.")
        print("Make sure it meets all the rules:")
        print("- Length between 6 and 16 characters")
        print("- At least one lowercase letter [a-z]")
        print("- At least one uppercase letter [A-Z]")
        print("- At least one number [0-9]")
        print("- At least one character from [$#@]")
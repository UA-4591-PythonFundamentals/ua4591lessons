password = input("Enter password: ")

has_lower = False
has_upper = False
has_digit = False
has_special = False


if len(password) < 6 or len(password) > 16:
    print("Password is invalid")
else:
    
    for ch in password:
        if ch.islower():
            has_lower = True
        elif ch.isupper():
            has_upper = True
        elif ch.isdigit():
            has_digit = True
        elif ch in "$#@":
            has_special = True

    
    if has_lower and has_upper and has_digit and has_special:
        print("Password is valid")
    else:
        print("Password is invalid")

def replace_number(number):
    if number == 1:
        return ("Monday")
    elif number == 2:
        return ("Tuesday")
    elif number == 3:
        return ("Wednesday")
    elif number == 4:
        return ("Thursday")
    elif number == 5:
        return ("Friday")
    elif number == 6:
        return ("Saturday")
    elif number == 7:
        return ("Sunday")
    else:
        raise ValueError ("The entered number is not between 1 and 8")

try: 
    user_input = input("Enter the number from 1 to 8, please: ")
    if user_input.isdigit():
        number = int(user_input)
        print(replace_number(number))
    else:
        raise TypeError ("Incorrect data type")
except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
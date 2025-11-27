def check_age(age):
    if age <= 0:
        raise ValueError("Incorrect value of age")
    else:
        if age % 2 == 0:
            return "Your age is an even number"
        else:
            return "Your age is an odd number"

try:
    user_input = input("Please, enter your age: ")
    if user_input.lstrip('-').isdigit():
        age = int(user_input)
        print(check_age(age))
    else:
        raise TypeError("Incorrect data type")

except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
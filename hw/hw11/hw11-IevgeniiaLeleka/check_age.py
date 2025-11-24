class NegativeNumber(Exception):
    pass

def check_age():

    try:
        age = int(input("Enter your age: "))
    except ValueError:
        return 'Please enter a valid age'

    if age < 0:
        raise NegativeNumber("Age cannot be negative number")
    elif age % 2 == 0:
        return "Your age is even"
    else:
        return "Your age is odd"


if __name__ == '__main__':
    try:
        print(check_age())
    except NegativeNumber as e:
        print(e)

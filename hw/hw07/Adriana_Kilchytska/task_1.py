def bigger_num (a, b):
    """ This function returns bigger number
        if numbers are equal function
        returns message
    """
    if a > b: 
        return a
    elif b > a: 
        return b
    else:
        equal = "Numbers are equal"
        return equal


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(bigger_num (a, b))
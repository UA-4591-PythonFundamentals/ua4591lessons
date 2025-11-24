def largest_number(a, b) :
    """
    Returns the largest of two numbers a and b.
    Args:
        a : The first number.
        b : The second number.
    Returns: The largest number of a and b.
    """
    if  a > b :
        return a
    else:
        return b
        
if __name__ == "__main__":
    a = int(input("Enter number a : "))
    b = int(input("Enter number b : "))
    print(largest_number(a, b))

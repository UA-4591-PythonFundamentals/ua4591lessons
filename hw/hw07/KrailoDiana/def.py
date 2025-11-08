# Task1.
def comparison(first, second):
    """ 
    This function compares two numbers
    entered by the user and selects the largest
    of them using the if...elif...else operators. 
    """
    if first > second:
        return f"The largest number is: {first}"
    elif second > first:
        return f"The largest number is: {second}"
    else:
        return "Numbers are equal"
    
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

result = comparison(first, second)
print(result)


# Task2.
def calculate_rectangle_area(length, height):
    """
    Сalculate and return the area of rectangle.
    """
    area = length * height
    return area

length = int(input("Enter the length: "))
height = int(input("Enter the height: "))

result = calculate_rectangle_area(length, height)
print(result)

def calculate_triangle_area(a, b, c):
    """
    Сalculate and return the area of triangle.
    """
    p = (a + b +c)/2
    area = (p * (p - a)*(p - b)*(p - c)) ** 0.5
    return area

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = calculate_triangle_area(a, b, c)
print(result)

def calculate_circle_area(r, pi=3.14):
    """
    Сalculate and return the area of circle.
    """
    area = pi*r**2
    return area

r = int(input("Enter radius: "))
result = calculate_circle_area(r)
print(result)


# Task3.
def calculate_the_number(string) -> str:
    """
    Calculate the number of charecters in a given string.
    """
    repetition = {}
    for i in string:
        if i in repetition:
            repetition[i] += 1
        else: 
            repetition[i] = 1
    return repetition
            
        
string = input("Enther the word: ").lower()
result = calculate_the_number(string)
print(result)
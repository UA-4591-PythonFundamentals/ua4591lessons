# Task1
def largest_number(a,b):
    """
    Function to find the largest number
    """
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return("They are equal.")

# a = largest_number(4,2)
# print(a)



# Task 2
import math
def triangle_area(a,h):
    return 0.5*a*h
def rectangle_area(a,b):
    return a*b
def circle_area(r):
    return round((math.pi*r**2), 3)

choice = input("Which figure area you want to calculate? Triangle, rectangle or circle?\n").lower()

if choice == "triangle":
    a = float(input("Enter the first side of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    print("The area of the triangle is", triangle_area(a,h))
elif choice == "rectangle":
    a = float(input("Enter the first side of the rectangle: "))
    b = float(input("Enter the second side of the rectangle: "))
    print("The area of the rectangle is", rectangle_area(a,b))

elif choice == "circle":
    r = float(input("Enter the radius of the circle: "))
    print("The area of the circle is", circle_area(r))
else:
    print("Invalid input")

# Task 3
def char_calc(text):
    my_dict = {}
    for char in text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict

# print(char_calc("hello"))


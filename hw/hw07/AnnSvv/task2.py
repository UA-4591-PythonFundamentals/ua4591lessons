#task2

user_figure = input("Enter the figure(rectangle, triangle or circle): ")

def area_rectangle(a, b):
    """calculate the area of rectangle"""
    area = a*b
    return area

def area_triangle(a, h):
    """calculate the area of triangle"""
    area = 1/2 * a*h
    return area

def area_circle(r):
    """calculate the area of circle"""
    PI = 3.14
    area = PI * (r**2)
    return area


if user_figure == "rectangle":
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    result = area_rectangle(a, b)
    print(f"The area of rectangle is {result}.")
elif user_figure == "triangle":
    a = int(input("Enter a: "))
    h = int(input("Enter h: "))
    result = area_triangle(a, h)
    print(f"The area of triangle is {result}.")
elif user_figure == "circle":
    r = int(input("Enter r: "))
    result = area_circle(r)
    print(f"The area of circle is {result}.")



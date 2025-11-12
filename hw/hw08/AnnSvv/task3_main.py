
from function import area_rectangle as rectangle, area_triangle as triangle, area_circle as circle

user_choice = input("Enter the figure (rectangle, triangle  or circle): ")


if user_choice == "rectangle":
    a = float(input("Enter a: "))
    b = float(input ("Enter b: "))
    rectangle(a,b)
elif user_choice == "triangle":
    h = float(input("Enter h: "))
    a = float(input ("Enter a: "))
    triangle(h,a)
elif user_choice == "circle":
    r= float(input("Enter r: "))
    circle(r)




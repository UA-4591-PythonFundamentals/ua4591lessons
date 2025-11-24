import functions
from functions import triangle_area, rectangle_area, circle_area

choice = input("What area of figure do you want to calculate? rectangle, triangle, circle\nYour choice: ").lower()
if choice == "rectangle":
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    print(rectangle_area(a,b))
elif choice == "triangle":
    a = float(input("Enter a:"))
    h = float(input("Enter h:"))
    print(triangle_area(a,h))
elif choice == "circle":
    r = float(input("Enter r:"))
    print(circle_area(r))
else:
    print("Invalid choice")
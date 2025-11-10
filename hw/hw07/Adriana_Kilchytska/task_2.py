import math

def rectangle_area(length ,width):
    return length*width

def triangle_area(base, height):
    return 0,5*base*height

def circle_area(radius):
    return math.pi*(radius**2)

print("What type of area do you want to calculate?")
choice = int(input("Enter 1 for rectangle, 2 for triangle, 3 for circle: "))

if choice == 1:
    a = float(input("Enter length: "))
    b = float(input("Enter width: "))
    print(rectangle_area(a, b))
elif choice == 2:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    print(triangle_area(b, h))
elif choice == 3:
    r = float(input("Enter radius: "))
    print(circle_area(r))
else:
    print("Error: incorrect number entered")

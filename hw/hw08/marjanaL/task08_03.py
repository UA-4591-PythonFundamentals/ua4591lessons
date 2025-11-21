from math import pi, pow
import module

msg = input("The area of which figure " \
"do you want to calculate?\n" \
"rectangle, triangle, circle \n")

if msg == "rectangle":
    a = int(input("Enter a, "))
    b = int(input("Enter b, "))
    module.rectangle_area(a, b)

elif msg == "triangle":
    a = int(input("Enter a, "))
    h = int(input("Enter h, "))
    module.triangle_area(h, a)

else:
    r = int(input("Enter r, "))
    module.circle_area(r)


from shapes import rectangle_area, triangle_area, circle_area
import math
from math import pow, pi

shape = input("Which figure area do you want to calculate? (rectangle, triangle, circle): ").strip().lower()

if shape == "rectangle":
    a = float(input("Enter length a: "))
    b = float(input("Enter width b: "))
    print("Area =", rectangle_area(a, b))

elif shape == "triangle":
    a = float(input("Enter base a: "))
    h = float(input("Enter height h: "))
    print("Area =", triangle_area(a, h))

elif shape == "circle":
    r = float(input("Enter radius r: "))
    print("Area =", circle_area(r))

else:
    print("Unknown figure")
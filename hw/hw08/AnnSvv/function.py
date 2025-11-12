from math import pi, pow

def area_rectangle(a,b):
    area = a*b
    return print(f"Area of rectangle is {area:.2f}.")

def area_triangle(h, a):
    area = 0.5 * h * a
    return print(f"Area of triangle is {area:.2f}.")

def area_circle(r):
    area = pi * pow(r, 2)
    return print(f"Area of circle is {area:.2f}.")


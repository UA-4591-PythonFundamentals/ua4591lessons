from math import pi, pow

def calculate_rectangle_area(a,b):
    """Calculates the area of a rectangle"""
    s = a*b
    return s

def calculate_triangle_area(h,a):
    """Calculates the area of a triangle"""
    s = 0.5*h*a
    return s

def calculate_circle_area(r):
    """Calculates the area of a circle"""
    s = pi*pow(r,2)
    return s
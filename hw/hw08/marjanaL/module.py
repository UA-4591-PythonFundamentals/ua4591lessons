from math import pi, pow
def rectangle_area(a, b):
   """this function calculates the area of rectangle"""
   area = a*b
   print(area)

def triangle_area(h, a):
   """this function calculates the area of triangle"""
   area = 0.5*h*a
   print(area)

def circle_area(r):
   """this function calculates the area of circle"""
   ar = pi*pow(r, 2)
   area = round(ar, 3)
   print(area)

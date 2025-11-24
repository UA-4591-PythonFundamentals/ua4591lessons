def rectangle_area(width, length):
   """this function calculates the area of rectangle"""
   area = width*length
   print(area)

def triangle_area(length, height):
   """this function calculates the area of triangle"""
   area = 1/2*length*height
   print(area)

def circle_area(radius):
   """this function calculates the area of circle"""
   pi=3.14
   area = pi*(radius**2)
   print(area)

rectangle_area(4, 2)
triangle_area(6, 4)
circle_area(7)
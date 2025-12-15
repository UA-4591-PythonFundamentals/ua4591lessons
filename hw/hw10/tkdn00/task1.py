# TASK1

class Polygon():
 def __init__(self, no_of_sides):
  self.n = no_of_sides
  self.sides = [0 for i in range(no_of_sides)]

 def input_sides(self):
  self.sides = [float(input(f"Enter side {str(i+1)}: "))
                for i in range(self.n)]

 def display_sides(self):
  for i in range(self.n):
   print(f"The side {i+1} = {self.sides[i]}")


class Rectangle(Polygon):
 def __init__(self):
  super().__init__(2)

 def find_area(self):
  a,b = self.sides
  area = a * b
  print(f"The area of the rectangle is {area}")



# a = Rectangle()
# a.input_sides()
# a.display_sides()
# a.find_area()
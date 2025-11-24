class Polygon:
    n = None

class Rectangle(Polygon):
    n = 4
    def __init__ (self, width, height):
        self.width = width
        self.height = height
    def square(self):
        s = self.width * self.height
        return s

r_width = int(input("Enter the width: "))
r_heigth = int(input("Enter the heigth: "))
r = Rectangle(r_width, r_heigth)
print("The square of rectangle is", r.square())
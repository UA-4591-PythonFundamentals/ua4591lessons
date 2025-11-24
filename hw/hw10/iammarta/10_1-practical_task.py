class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        sides = [width, height, width, height]
        super().__init__(sides)

    def area(self):
        return self.width * self.height

# ---- EXAMPLES OF USE ----
rect = Rectangle(5, 3)
print("Sides:", rect.sides)          
print("Perimeter:", rect.perimeter()) 
print("Area:", rect.area())

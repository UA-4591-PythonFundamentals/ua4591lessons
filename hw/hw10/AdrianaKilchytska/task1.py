class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, width, length):
        super().__init__(4)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
rect = Rectangle(10, 20)
print(f"Area of rectangle: {rect.area()}")
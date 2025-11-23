class Polygon():
    def __init__(self, n_sides):
        self.n_sides = n_sides
        
class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(n_sides=4)
        self.width = width
        self.height = height

    def area(self):
        area = self.width*self.height
        return area
    
rect = Rectangle(10, 8)
area = rect.area()
print(f"The area of rectangle is {area}.")
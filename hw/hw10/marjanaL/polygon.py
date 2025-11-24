class Polygon:
    def __init__(self, *sides):
        self.sides = sides
        
class Rectangle(Polygon):
    def __init__(self, width, length):
        super().__init__([width, length])
        self.width = width
        self.length = length

    def square_of_rect(self):
        square = self.width*self.length
        return square

r1 = Rectangle(4, 5)
square_r1 = r1.square_of_rect()
print(f'The square of rectangle is {square_r1}')

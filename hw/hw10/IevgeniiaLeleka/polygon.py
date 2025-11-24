class Polygon:
    def __init__(self, n):
        self.n = n

class Rectangle(Polygon):
    def __init__(self, width, length):
        super().__init__(4)
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length


if __name__ == "__main__":
    rect = Rectangle(20,30)
    print(rect.area())

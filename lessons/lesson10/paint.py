from random import randint
import re
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    def __repr__(self):
        return f"({self.x}, {self.y})"
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def add(self, other):
        return Point(self.x + other.x, self.y + other.y)
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
class ColorPoint(Point):
    def __init__(self, x=0, y=0, color=(0, 0, 0)):
        super().__init__(x, y)
        self.color = color

    def __str__(self):
        return f"ColorPoint({self.x}, {self.y}, {self.color})"
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.color})"






# point = Point(5, 10)
# points = [Point(randint(-10, 10), randint(-10, 10)) for i in range(5)]

# print("Single Point:", point)
# print("Points List:", points)
# p2 = points[1] + point
# # p2 = points[1].__add__(point)
# print("Added Point:", p2)
# points.sort()
# print("Sorted Points List:", points)
# p2 = points[1].add(point)
# print("Added Point using add method:", p2)
# print(p2.__repr__())
# # print(p2.__dict__)
# # print(Point.__dict__)


points = [
    Point(randint(-10, 10), randint(-10, 10)) 
    if randint(0,1) else
    ColorPoint(randint(-10, 10),randint(-10, 10), (randint(0,255),
                                                   randint(0,255),
                                                   randint(0,255)))
    for i in range(5)
]

print("Points List with ColorPoints:", points)

for point in points:
    print(f"{point} distance from origin: {point.distance_from_origin()}")
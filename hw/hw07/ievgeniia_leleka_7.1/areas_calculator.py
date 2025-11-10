import math

def triangle_area(base:float, height:float) -> float:
    """Return the area of a triangle."""
    return 0.5 * base * height

def rectangle_area(length:float, width:float) -> float:
    """Return the area of a rectangle."""
    return length * width

def circle_area(radius:float) -> float:
    """Return the area of a circle."""
    return math.pi * radius**2

if __name__ == "__main__":
    print("Area of a triangle is", triangle_area(10, 70))
    print("Area of a rectangle is", rectangle_area(5, 7))
    print("Area of a circle is", circle_area(15))

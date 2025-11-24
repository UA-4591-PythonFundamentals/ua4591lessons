import math
from areas_calculator import triangle_area, rectangle_area, circle_area

def test_triangle_area():
    assert triangle_area(10, 5) == 25.0
    assert triangle_area(3, 4) == 6.0
    assert triangle_area(0, 5) == 0.0

def test_rectangle_area():
    assert rectangle_area(8, 4) == 32.0
    assert rectangle_area(5, 5) == 25.0
    assert rectangle_area(0, 10) == 0.0

def test_circle_area():
    assert math.isclose(circle_area(1), math.pi, rel_tol=1e-9)
    assert math.isclose(circle_area(0), 0.0, rel_tol=1e-9)
    assert math.isclose(circle_area(2.5), math.pi * 2.5**2, rel_tol=1e-9)

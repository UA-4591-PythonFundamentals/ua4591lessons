def circle_area(r: float, pi: float, pow_func) -> float:
    """Calculate the area of a circle.
    
    Args:
        r (float): The radius of the circle
        pi (float): The value of pi
        pow_func (function): The function to raise the radius to the power of 2
    Returns:
        float: The area of the circle rounded to 2 decimal places
    """
    s = pi * pow_func(r,2)
    return round(s, 2)

def triangle_area(a: float, b: float) -> float:
    """Calculate the area of a triangle.
    
    Args:
        a (float): The base of the triangle
        b (float): The height of the triangle
    
    Returns:
        float: The area of the triangle rounded to 2 decimal places
    """
    s = 0.5 * a * b
    return round(s, 2)


def rectangle_area(a: float, b: float) -> float:
    """Calculate the area of a rectangle.
    
    Args:
        a (float): The width of the rectangle
        b (float): The height of the rectangle
    
    Returns:
        float: The area of the rectangle rounded to 2 decimal places
    """
    s = a * b
    return round(s, 2)

def rectangle_area_calc() :
    """
    Returns calculate rectangle area (rectangle_area = length * width).
    """
    rectangle_area = length * width
    return f"rectangle area is {rectangle_area} "

def triangle_area_calc() :
    """
    Returns calculate triangle area (triangle_area = (base * height) / 2).
    """
    triangle_area = (base * height) / 2
    return f"triangle area is {triangle_area} "

def circle_area_calc() :
    """
    Returns calculate circle area (circle_area = 3.14 * (radius**2)).
    """
    circle_area = 3.14 * (radius**2)
    return f"circle area is {circle_area} "

if __name__ == "__main__":
    
    print("Choose a shape to calculate the area: \n1. Rectangle \n2. Triangle \n3. Circle")
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        length = float(input("Enter length of rectangle : "))
        width = float(input("Enter width of rectangle : "))
        print(rectangle_area_calc())

    elif choice == "2":
        base = float(input("Enter base of triangle : "))
        height = float(input("Enter height of triangle : "))
        print(triangle_area_calc())

    elif choice == "3":
        radius = float(input("Enter radius of circle : "))
        print(circle_area_calc())

    else:
        print("Invalid choice!")
    
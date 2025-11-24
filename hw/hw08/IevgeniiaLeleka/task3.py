from area_calc import rectangle_area, circle_area, triangle_area

def area_calculator():
    shape = input("Enter shape (rectangle/triangle/circle): ")

    match shape:
        case "rectangle":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            return rectangle_area(length, width)

        case "triangle":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            return triangle_area(base, height)

        case "circle":
            radius = float(input("Enter radius: "))
            return circle_area(radius)

        case _ :
            return "Enter a valid shape"

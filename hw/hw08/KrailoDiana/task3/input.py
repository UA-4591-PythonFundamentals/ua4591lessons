import area

def main():

    print("Select the area you need to calculate")
    shape = int(input("If you need to calculate the area of \n" \
                    "rectangle - press 1 \n" \
                    "triangle - press 2 \n" \
                    "circle - press 3 \n"))

    if shape == 1:
        a = float(input("Enter the a: "))
        b = float(input("Enter the b: "))
        print(area.calculate_rectangle_area(a,b))

    elif shape == 2:
        h = float(input("Enter the hight: "))
        a = float(input("Enter the a: "))
        print(area.calculate_triangle_area(h,a))

    elif shape == 3:
        r = float(input("Enter the radius: "))
        print(area.calculate_circle_area(r))

    else:
        print("Please select the correct value from 1 to 3")


if __name__ == "__main__":
    main()
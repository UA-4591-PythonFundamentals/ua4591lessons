import shapes_area

def run_calculator():
    
    print("--- Area Calculator ---")
    print("Which figure's area do you want to calculate?")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("ENTER YOUR CHOICE (1, 2, or 3): ")
    
    print("-" * 20) 

    try:
        if choice == '1':
            print("You chose: Rectangle (S = a * b)")
            a = float(input("Enter the length of side 'a': "))
            b = float(input("Enter the length of side 'b': "))
            
            result = shapes_area.rectangle_area(a, b)
            print(f"Result: The area of the rectangle is = {result}")

        elif choice == '2':
            print("You chose: Triangle (S = 0.5 * h * a)")
            h = float(input("Enter the height 'h': "))
            a = float(input("Enter the length of the base 'a': "))
            
            result = shapes_area.triangle_area(h, a)
            print(f"Result: The area of the triangle is = {result}")

        elif choice == '3':
            print("You chose: Circle (S = pi * r^2)")
            r = float(input("Enter the radius 'r': "))
            
            result = shapes_area.circle_area(r)
            print(f"Result: The area of the circle is = {result:.2f}")

        else:
            print("Error: Invalid choice.")
            print("Please run the program again and select 1, 2, or 3.")

    except ValueError:
        print("\nError: You did not enter a number.")
        print("Please run the program again.")

if __name__ == "__main__":
    run_calculator()
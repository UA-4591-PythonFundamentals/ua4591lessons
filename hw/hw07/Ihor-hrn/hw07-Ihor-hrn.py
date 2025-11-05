## Task1

def larg_num(num1: int | float, num2: int | float) -> int | str:
    """Returns the largest numbers of two numbers
    Args:
        num1 (int|float): The first number
        num2 (int|float): The second number
    Returns:
        int: The largest number
        str: If the input is not a number
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        # хоча порівнювати можна будь-які символи в задачі вказано лише числа
        return "Помилка: введені дані не є числами"
    else:
        if num1 > num2:
            return num1
        elif num2 > num1:
            return num2
        else:
            return "Числа рівні"

# print(larg_num(100, 2))

## Task2

def parse_float(s: str) -> float|None:
    """Parse a string to a float number.
    Args:
        s (str): The string to parse
    Returns:
        float: The float number
        None: If the string is not a valid float number
    """
    s = s.strip().replace(',', '.')
    if s.count('.') <= 1 and s.replace('.', '').isdigit():
        value = float(s)
        return value
    else:
        return None

def circle_area() -> float|str:
    """Calculate the area of a circle based on user input.
    
    Prompts the user to enter a radius and calculates the area using the formula π * r².
    Continues to prompt until a valid positive number is entered.
    
    Returns:
        float: The area of the circle rounded to 2 decimal places
        str: Error message if invalid radius is provided
    """
    PI = 3.14
    
    while True:
        radius = parse_float(input("\tВведіть радіус: "))
        if radius is None:
            print("Введіть число!")
            continue
        if radius <= 0:
            return "Error: Invalid radius"
        s = PI * radius**2
        result = round(s, 2)
        return result

def triangle_area() -> float|str:
    """Calculate the area of a triangle based on user input.
    
    Prompts the user to enter base and height values and calculates the area 
    using the formula 0.5 * base * height. Continues to prompt until valid 
    positive numbers are entered.
    
    Returns:
        float: The area of the triangle rounded to 2 decimal places
        str: Error message if invalid input is provided
    """
    while True:
        base = parse_float(input("\tВведіть основу: "))
        height = parse_float(input("\tВведіть висоту: "))
        if base is None or height is None:
            print("Помилка: введені дані не є числами")
            continue
        if base <= 0 or height <= 0:
            print("Помилка: введені дані не є додатними числами")
            continue
        s = 0.5 * base * height
        return round(s, 2)


def rectangle_area() -> float|str:
    """Calculate the area of a rectangle based on user input.
    
    Prompts the user to enter width and height values and calculates the area 
    using the formula width * height. Continues to prompt until valid 
    positive numbers are entered.
    
    Returns:
        float: The area of the rectangle rounded to 2 decimal places
        str: Error message if invalid input is provided
    """
    while True:
        width = parse_float(input("\tВведіть ширину: "))
        height = parse_float(input("\tВведіть висоту: "))
        if width is None or height is None:
            print("Помилка: введені дані не є числами")
            continue
        if width <= 0 or height <= 0:
            print("Помилка: введені дані не є додатними числами")
            continue
        s = width * height
        return round(s, 2)


def main():
    """Main function that provides a menu interface for area calculations.
    
    Displays a menu allowing users to choose between calculating areas of:
    - Circle (option 1)
    - Triangle (option 2) 
    - Rectangle (option 3)
    - Exit (Enter key)
    
    The function recursively calls itself to allow multiple calculations,
    but limits usage to 5 attempts before showing a trial period message.
    """
    bad = 0
    while True:
        print('Для розрахунку площі кола натисніть 1' \
        '\nдля розрахунку площі трикутника натисніть 2' \
        '\nдля розрахунку площі прямокутника натисніть 3' \
        '\nДля виходу натисніть "Enter"')
        num = input().strip()

        if num == '1':
            result = circle_area()
            print(f"\n\tПлоща кола: {result}\n")
            bad = 0

        elif num == '2':
            result = triangle_area()
            print(f"\n\tПлоща трикутника: {result}\n")
            bad = 0

        elif num == '3': 
            result = rectangle_area()
            print(f"\n\tПлоща прямокутника: {result}\n")
            bad = 0

        elif num == '':
            print("Гарного дня!)")
            return

        else:
            print('Введіть 1, 2, 3' \
            '\nДля виходу натисніть "Enter"')
            bad +=1
            if bad >= 3:
                print("\n\033[91mДосягнуто максимальної кількості спроб!\033[0m\n")
                print(f"{bad} спроб використано")
                return
           
# main()

## Task3

def calculate_char() -> dict:
    """Calculate the number of characters in a word.
    Args:
        None
    Returns:
        dict: A dictionary with the number of characters in the word
        str: If the input is not a string
    """
    word = input("Введіть слово: ")
    if not isinstance(word, str):
        return "Помилка: введені дані не є рядком"
    x = {}
    for el in word:
        x[el] = word.count(el)
    print(x)
    return x

# calculate_char()
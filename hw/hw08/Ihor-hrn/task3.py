import calculation_module as cm
import math

def parse_float(s: str) -> float | None:
    """Parse a string to float, handling comma as decimal separator.
    
    Args:
        s (str): String to parse as float
        
    Returns:
        float | None: Parsed float value or None if parsing fails
    """
    s = s.strip().replace(',', '.')
    if s.count('.') <= 1 and s.replace('.', '').isdigit():
        return float(s)
    return None

def main_calculations() -> None:
    """Main function that provides a menu interface for area calculations.
    
    Displays a menu allowing users to choose between calculating areas of:
    - Circle (option 1)
    - Triangle (option 2) 
    - Rectangle (option 3)
    - Exit (Enter key)
    
    The function continues in a loop to allow multiple calculations,
    but limits invalid input attempts to 3 before terminating.
    
    Returns:
        None
    """
    bad = 0
    while True:
        print('Для розрахунку площі кола натисніть 1' \
        '\nдля розрахунку площі трикутника натисніть 2' \
        '\nдля розрахунку площі прямокутника натисніть 3' \
        '\nДля виходу натисніть "Enter"')
        num = input().strip()

        if num == '1':
            r = parse_float(input("Введіть радіус кола: "))
            if r is None or r <= 0:
                print("Помилка: радіус має бути додатним числом\n")
                continue
            result = cm.circle_area(r, math.pi, math.pow)
            print(f"\n\tПлоща кола: {result}\n")
            bad = 0

        elif num == '2':
            a = parse_float(input("Введіть основу: "))
            b = parse_float(input("Введіть висоту: "))
            if a is None or b is None or a <= 0 or b <= 0:
                print("Помилка: введіть додатні числа\n")
                continue
            result = cm.triangle_area(a, b)
            print(f"\n\tПлоща трикутника: {result}\n")
            bad = 0

        elif num == '3': 
            a = parse_float(input("Введіть ширину: "))
            b = parse_float(input("Введіть висоту: "))
            if a is None or b is None or a <= 0 or b <= 0:
                print("Помилка: введіть додатні числа\n")
                continue
            result = cm.rectangle_area(a, b)
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

if __name__ == "__main__":
    main_calculations()
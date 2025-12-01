from math import sqrt
def solve_quadratic_equation(a, b, c):
    """
    Розв'язує квадратне рівняння виду ax^2 + bx + c = 0
    і повертає корені.
    """
    if a == 0:
        return None

    D = b**2 - 4*a*c

    if D > 0:
        x1 = (-b + sqrt(D)) / (2*a)
        x2 = (-b - sqrt(D)) / (2*a)
        return x1, x2
    elif D == 0:
        x = -b / (2*a)
        return x
    else:
        return None


def shufle_list(lst):
    """
    Перемішує елементи списку випадковим чином.
    """
    import random
    random.shuffle(lst)
    return lst

if __name__ == "__main__":
    a = float(input("Введіть коефіцієнт a: "))
    b = float(input("Введіть коефіцієнт b: "))
    c = float(input("Введіть коефіцієнт c: "))

    result = solve_quadratic_equation(a, b, c)
    print(result)
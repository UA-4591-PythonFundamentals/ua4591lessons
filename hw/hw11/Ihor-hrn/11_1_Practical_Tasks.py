"""Task1"""
def check_age(user_age):
    user_age = int(user_age)
    if user_age < 0:
        raise ValueError
    if user_age % 2 == 0:
        return f"{user_age} парне"
    else:
        return f"{user_age} непарне"


while True:
    try:
        user_age = input("Введіть вік: ")
        result = check_age(user_age)
        print(result)
        break
    except ValueError:
        print("\tВведіть вік")

"""Task2"""

while True:
    try:
        user_input = int(input("Введіть день тижня числом (1-Понеділок, 2-Вівторок ...): "))
        if user_input not in range(1, 8):
            raise ValueError
        week = {1:'Понеділок', 2:'Вівторок', 
                3:'Середа', 4:'Четвер', 
                5:'П\'ятниця', 6:'Субота', 
                7:'Неділя'}
        print(week[user_input])
        break
    except ValueError:
        print("\tВведіть число від 1 до 7.")
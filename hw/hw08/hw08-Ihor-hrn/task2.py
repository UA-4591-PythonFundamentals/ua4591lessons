import re
    
def password_check() -> str:
    """
    Перевіряє пароль на відповідність вимогам безпеки.
    
    Функція запитує у користувача пароль і перевіряє його на наступні критерії:
    - Наявність літер нижнього регістру (a-z)
    - Наявність літер верхнього регістру (A-Z)
    - Наявність цифр (0-9)
    - Наявність спеціальних символів (@$#)
    - Довжина від 6 до 16 символів
    
    Якщо пароль не відповідає будь-якому з критеріїв, функція виводить
    відповідне повідомлення про помилку і запитує пароль знову.
    
    Returns:
        str: Валідний пароль, який відповідає всім вимогам.
    """
    while True:
        password = input("Введіть пароль: ")
        result = re.findall(r'[a-z]', password)
        if not result:
            print("Відсутні літери нижнього регістру \"a-z\"!")
            continue
        result = re.findall(r'[A-Z]', password)
        if not result:
            print("Відсутні літери верхнього регістру \"A-Z\"!")
            continue
        result = re.findall(r'[0-9]', password)
        if not result:
            print("Відсутні числа \"0-9\"!")
            continue
        result = re.findall(r'[@$#]', password)
        if not result:
            print("Відсутні симовли \"@$#\"!")
            continue
        if len(password) < 6:
            print("Замала к-сть символів в паролі!")
            continue
        if len(password) > 16:
            print("Завелика к-сть символів в паролі!")
            continue
        else:
            print('Пароль правильний!')
            print(password)
            return password
    
password_check()
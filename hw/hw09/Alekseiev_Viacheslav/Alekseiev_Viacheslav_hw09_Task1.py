from random import randint

# Загадываем число
secret_number = randint(1, 100)

attempts = 10

print("I guessed a number from 1 to 100.")
print("You have 10 attempts to guess it.")

# Игра
for attempt in range(1, attempts + 1):
    user_input = input(f"Attempt {attempt}. Enter your number: ")

    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(user_input)

    if guess < secret_number:
        print("My number is greater.")
    elif guess > secret_number:
        print("My number is less.")
    else:
        print("Congratulations! You guessed the number!")
        break
else:
    print("You have used all 10 attempts.")
    print("The number was:", secret_number)

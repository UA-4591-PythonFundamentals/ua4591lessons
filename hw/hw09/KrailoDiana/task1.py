import random 

lose = """
=================================================
                      ,______
                      |---.  |
              ___     |    `/
             / .-\\  ./=)
            |  |"|_/\\/|
            ;  |-;| /_|
           / \\_| |/ \\ |
          /      \\/\\( |
          |   /  |` ) |
          /   \\ _/    |
         /--._/  \\    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \\  |
       (_.-.__.__./  /
=================================================
"""

print("=================================================")
print("WELCOME TO THE GUESS THE NUMBER GAME!")
print("You need to guess a number between 1 and 100.")
print("You have only 10 attempts.")
print("Good luck!")
print("=================================================")

gen_number = random.randint(1, 100)

lives = 10

game_over = False

while not game_over:
    print(f"{lives}/10 LIVES LEFT")
    guess = int(input("Enter the number: "))
    
    if guess > gen_number:
        print("Your number is greater than the generated number")
        lives -= 1
    elif guess < gen_number:
        print("Your number is less than the generated number ")
        lives -= 1
    elif guess == gen_number:
        game_over = True
        print("You guess the number! YOU WIN!")

    if lives == 0:
        game_over = True
        print(f"IT WAS {gen_number}. YOU LOSE! \n {lose}")
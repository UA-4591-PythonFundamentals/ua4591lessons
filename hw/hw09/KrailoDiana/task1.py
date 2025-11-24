import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Guess the Number")
font = pygame.font.SysFont("consolas", 14)

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
show_lose_screen = False

gen_number = random.randint(1, 100)
lives = 10
game_over = False

console_output = [
    "=================================================",
    "WELCOME TO THE GUESS THE NUMBER GAME!",
    "You need to guess a number between 1 and 100.",
    "You have only 10 attempts.",
    "Good luck!",
    "=================================================",
    "Press ENTER to begin",
    "To save the number, press ENTER again.",
]

user_input = ""
game_state = 1

def render_console():
    screen.fill((20, 20, 20))

    y = 20
    for line in console_output[-15:]:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (20, y))
        y += 28

    if game_state == 2:
        input_text = font.render(f"Enter the number: {user_input}", True, (0, 255, 0))
        screen.blit(input_text, (20, 470))

    if show_lose_screen:
        screen.fill((20, 20, 20))

        lose_text = font.render(f"IT WAS {gen_number}. YOU LOSE!", True, (255, 255, 255))
        screen.blit(lose_text, (20, 30))

        y = 80
        for line in lose.split("\n"):
            text = font.render(line, True, (255, 255, 255))
            screen.blit(text, (20, y))
            y += 18

        pygame.display.update()
        return

    pygame.display.update()


running = True
while running:
    render_console()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_over:
            continue

        if event.type == pygame.KEYDOWN:
            if game_state == 1:
                if event.key == pygame.K_RETURN:
                    console_output.append("Waiting for your input...")
                    game_state = 2
                continue

            if game_state == 2:
                if event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]

                elif event.key == pygame.K_RETURN:
                    if user_input.isdigit():
                        guess = int(user_input)
                        console_output.append(f"You entered: {guess}")
                        console_output.append(f"{lives}/10 LIVES LEFT")

                        if guess > gen_number:
                            console_output.append("Your number is greater than the generated number")
                            lives -= 1

                        elif guess < gen_number:
                            console_output.append("Your number is less than the generated number")
                            lives -= 1

                        else:
                            console_output.append("You guessed the number! YOU WIN!")
                            game_over = True

                        user_input = ""

                        if lives == 0 and not game_over:
                            game_over = True
                            show_lose_screen = True

                        if not game_over:
                            console_output.append("Waiting for your input...")

                    else:
                        console_output.append("Enter NUMBERS ONLY!")
                        user_input = ""

                else:
                    if event.unicode.isdigit():
                        user_input += event.unicode
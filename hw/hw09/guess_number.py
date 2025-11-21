import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Number Guessing Game")

font = pygame.font.SysFont("Arial", 28)
small_font = pygame.font.SysFont("Arial", 22)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

secret_number = random.randint(1, 100)
attempts_left = 10
user_input = ""
message = "Guess a number from 1 to 100:"

def draw():
    screen.fill(WHITE)

    text = font.render(message, True, BLACK)
    screen.blit(text, (20, 40))

    input_text = font.render(f'Enter a number: {user_input}', True, BLACK)
    screen.blit(input_text, (20, 100))

    attempts_text = small_font.render(f"Attempts left: {attempts_left}", True, BLACK)
    screen.blit(attempts_text, (20, 160))

    pygame.display.flip()


running = True
while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.unicode.isdigit():
                user_input += event.unicode

            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            if event.key == pygame.K_RETURN:
                if user_input == "":
                    break

                guess = int(user_input)
                user_input = ""
                attempts_left -= 1

                if guess == secret_number:
                    message = f"Correct! The number was {secret_number}!"
                    draw()
                    pygame.time.delay(3000)
                    running = False
                elif guess < secret_number:
                    message = "Too LOW! Try again:"
                else:
                    message = "Too HIGH! Try again:"

                if attempts_left == 0 and guess != secret_number:
                    message = f"Out of attempts! Number was {secret_number}."
                    draw()
                    pygame.time.delay(3000)
                    running = False

pygame.quit()

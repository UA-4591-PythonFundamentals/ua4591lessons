import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess Game!!!")

font = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

secret_number = random.randint(1, 100)
attempts = 10
current_text = ''
message = 'Guess a number between 1 and 100:'
game_over = False

running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if current_text.isdigit():
                    guess = int(current_text)
                    attempts -= 1
                    if guess < secret_number:
                        message = "The number is greater than your guess."
                    elif guess > secret_number:
                        message = "The number is less than your guess."
                    else:
                        message = f"Congratulations! You guessed {secret_number}!"
                        game_over = True
                    current_text = ''
                    if attempts == 0 and not game_over:
                        message = f"Game over! The number was {secret_number}."
                        game_over = True
                else:
                    message = "Please enter a valid number."
                    current_text = ''
            elif event.key == pygame.K_BACKSPACE:
                current_text = current_text[:-1]
            else:
                current_text += event.unicode

    input_surface = font.render("Your guess: " + current_text, True, BLACK)
    message_surface = font.render(message, True, BLACK)
    attempts_surface = font.render(f"Attempts left: {attempts}", True, BLACK)

    screen.blit(input_surface, (50, 150))
    screen.blit(message_surface, (50, 100))
    screen.blit(attempts_surface, (50, 200))

    pygame.display.flip()

pygame.quit()

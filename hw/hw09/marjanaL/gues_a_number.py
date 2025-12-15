import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Guess a number')
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 34)
OLIVE = (128, 128, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

number = randint(1, 100)
user_input_string = ""
message = "Can you guess a number from 1 to 100 in 10 tries?"
feedback_message = ""
tries_left = 10

game_active = True

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if game_active:
                if event.key == pygame.K_RETURN:
                    user_guess = int(user_input_string)
                    if 1 <= user_guess <= 100:
                        if user_guess > number:
                            feedback_message = "Your guess is too high!"
                            user_input_string = ""
                        elif user_guess < number:
                            feedback_message = "Your guess is too low!"
                            user_input_string = ""
                        else:
                            feedback_message = "You win!"
                            game_active = False
                            user_input_string = ""

                        if game_active:
                            tries_left -= 1
                            if tries_left == 0 and user_guess != number:
                                feedback_message = f"Game Over! The number was {number}."
                                game_active = False
                        else:
                            user_input_string = ""

                    else:
                        feedback_message = "Please enter a number between 1 and 100."
                        user_input_string = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input_string = user_input_string[:-1]
                else:
                    if event.unicode.isdigit() and len(user_input_string) < 3:
                        user_input_string += event.unicode

    screen.fill(OLIVE)

    text_surface = font.render(message, True, BLACK)
    screen.blit(text_surface, (100, 50))

    tries_text = font.render(f"Tries left: {tries_left}", True, BLACK)
    screen.blit(tries_text, (50, 100))

    input_prompt = font.render("Your guess: ", True, BLACK)
    screen.blit(input_prompt, (200, 250))
    input_surface = font.render(user_input_string, True, WHITE)
    screen.blit(input_surface, (380, 250))

    feedback_surface = font.render(feedback_message, True, BLACK)
    screen.blit(feedback_surface, (200, 350))

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
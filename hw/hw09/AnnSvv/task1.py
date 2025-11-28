import pygame 
import sys 
from random import randint

pygame.init()

width = 600
height = 600 
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Guess number")

WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
INPUT_BOX_COLOR = (180, 180, 180)

screen.fill(WHITE)
pygame.display.flip()

clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 38)
small_font = pygame.font.SysFont("arial", 24)


number_guess = randint(1, 100)
max_tries = 10
tries_left = max_tries
game_over = False
message = ("Try to guess the number from 1 to 100")
user_input = ""
guesses =[]

input_box = pygame.Rect(200, 450, 200, 40)

def display_text(text, font_style, color, surface, x, y):
    textobj = font_style.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_RETURN:
                    try:
                        guess = int(user_input)
                        guesses.append(guess)
                        tries_left-=1

                        if guess == number_guess:
                            message = (f"Congratulations! You guessed the number: {number_guess}!")
                            game_over = True
                        elif guess <number_guess:
                            message = (f"The number is higher.")
                        elif guess >number_guess:
                            message = (f"The number is lower.")

                        if tries_left ==0 and not game_over:
                            message = (f"The game is over! You didn't guess the number. The number is {number_guess}. ")
                            game_over = True
                        user_input = ""    
                    except ValueError:
                        message = "You entered invalid data."
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    if event.unicode.isdigit():
                        user_input+=event.unicode
    
    screen.fill(WHITE) 
    
    display_text("Guess the Number", font, BLACK, screen, width // 2, 50)
    display_text(message, small_font, RED, screen, width // 2, 200)
    display_text(f"Attempts left: {tries_left}", small_font, GREEN, screen, width // 2, 250)
    
    pygame.draw.rect(screen, INPUT_BOX_COLOR, input_box, 2)

    text_surface = small_font.render(user_input, True, BLACK)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    input_box.w = max(200, text_surface.get_width() + 10)

    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()

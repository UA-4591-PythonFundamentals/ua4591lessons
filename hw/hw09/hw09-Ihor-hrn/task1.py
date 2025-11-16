import random
import pygame

pygame.init()

game_screen = pygame.display.set_mode((300, 140))
clock = pygame.time.Clock()
FPS = 20
input_text = ""

color = {
    'RED': (255, 0, 0),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'GRAY': (195, 182, 182)
}

game_over = False
attempts = 10
random_num = random.randint(1, 100)

arr = []
input_text = ''
message = ''
hint_message = ""
guess = None

while not game_over:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE and input_text != '':
                input_text = input_text[:-1]

            if event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3,
                            pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, 
                            pygame.K_8, pygame.K_9, pygame.K_KP0, 
                            pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, 
                            pygame.K_KP4, pygame.K_KP5, pygame.K_KP6, 
                            pygame.K_KP7, pygame.K_KP8, pygame.K_KP9]:
                # Mapping pygame keys to their numeric values
                key_to_digit = {
                    pygame.K_0: '0', pygame.K_1: '1', pygame.K_2: '2', pygame.K_3: '3',
                    pygame.K_4: '4', pygame.K_5: '5', pygame.K_6: '6', pygame.K_7: '7',
                    pygame.K_8: '8', pygame.K_9: '9', pygame.K_KP0: '0',
                    pygame.K_KP1: '1', pygame.K_KP2: '2', pygame.K_KP3: '3',
                    pygame.K_KP4: '4', pygame.K_KP5: '5', pygame.K_KP6: '6',
                    pygame.K_KP7: '7', pygame.K_KP8: '8', pygame.K_KP9: '9'
                }
                input_text = input_text + key_to_digit[event.key]

            if event.key in (pygame.K_KP_ENTER, pygame.K_RETURN):

                if input_text != '':
                    guess = input_text
                    input_text = ""

                if guess is None:
                    message = "Введіть число від 1 до 100"

                elif int(guess) < random_num:
                    message = "Ваше число менше"
                    attempts -= 1

                elif int(guess) > random_num:
                    message = "Ваше число більше"
                    attempts -= 1

                elif int(guess) == random_num:
                    message = "Ви вгадали!"


    if attempts == 0 or message == "Ви вгадали!":
        game_over = True

    game_screen.fill(color['WHITE'])

    font = pygame.font.SysFont(None, 30)

    attempts_text = font.render(f"Спроб: {attempts}", True, color['BLACK'])
    game_screen.blit(attempts_text, (10, 10))
    score_text = font.render(f"Введіть число: {input_text}", True, color['BLACK'])
    game_screen.blit(score_text, (10, 40))

    message_text = font.render(f"{message}", True, color['BLACK'])
    game_screen.blit(message_text, (10, 100))

    if guess is not None:
        score_text = font.render(f"Ваше число: {guess}", True, color['BLACK'])
        game_screen.blit(score_text, (10, 70))


    pygame.display.update()
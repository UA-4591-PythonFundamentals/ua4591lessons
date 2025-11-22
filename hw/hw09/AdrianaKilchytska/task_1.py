import pygame
import random

pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Вгадай число")

font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 50)  

number_to_guess = random.randint(1, 100)
attempts = 10
user_text = ""
message = "Введіть число (1-100)"

game_over = False
won = False  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if user_text:
                    guess = int(user_text)
                    
                    if guess == number_to_guess:
                        message = "Вітаю з виграшем!"
                        game_over = True
                        won = True
                    else:
                        attempts -= 1
                        if attempts == 0:
                            message = f"Ви програли! Число: {number_to_guess}"
                            game_over = True
                            won = False
                        elif guess < number_to_guess:
                            message = "Моє число БІЛЬШЕ"
                        else:
                            message = "Моє число МЕНШЕ"
                    
                    user_text = ""
            
            elif event.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            else:
                if event.unicode.isdigit():
                    user_text += event.unicode

    screen.fill((50, 50, 50)) 

    if game_over:        
        if won:
            color = (100, 255, 100)
        else:
            color = (255, 80, 80)
            
        end_surf = big_font.render(message, True, color)
        
        text_rect = end_surf.get_rect(center=(300, 200))
        screen.blit(end_surf, text_rect)
        
    else:        
        msg_surface = font.render(message, True, (255, 255, 255))
        msg_rect = msg_surface.get_rect(center=(300, 100))
        screen.blit(msg_surface, msg_rect)
        
        input_surface = font.render(f"Ваше число: {user_text}", True, (100, 255, 100))
        input_rect = input_surface.get_rect(center=(300, 200))
        screen.blit(input_surface, input_rect)
        
        attempts_surface = font.render(f"Спроб залишилось: {attempts}", True, (200, 200, 200))
        screen.blit(attempts_surface, (20, 20))

    pygame.display.flip()

pygame.quit()
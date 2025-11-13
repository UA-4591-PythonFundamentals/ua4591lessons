import pygame
from random import randint

from colors import COLORS


pygame.init()


font = pygame.font.SysFont('Calibri', 25, True, False)

width = 800
height = 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('My Game')


tank_pos = [width//2, height-10]
tanks_bullets = []


NLO = []



clock = pygame.time.Clock()
FPS = 20
run = True

mouse_1_down = 0




while run:

# event handling
    for event in pygame.event.get():
        # print(f"Event: {event}")
        match event.type:
            case pygame.QUIT:
                run = False
        
            case pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_1_down = 1
                    tanks_bullets.append([tank_pos[0], tank_pos[1]-5])
            case pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    mouse_1_down = 0
                    
                
            # case pygame.MOUSEMOTION:
            #     print(f"Mouse moved to {event.pos} with rel {event.rel} and buttons {event.buttons}")
            case _:
                pass
        if mouse_1_down:
            if mouse_1_down % 2 == 0:
                tanks_bullets.append([tank_pos[0], tank_pos[1]-5])
            mouse_1_down += 1
    
# game logic
    gameDisplay.fill(COLORS["white"])  # Fill the screen with white
    for nlo in NLO:
        nlo[1] += 1
        nlo[0] += randint(-5, 5)
        pygame.draw.rect(gameDisplay, COLORS["black"], (nlo[0], nlo[1], 20, 10))
    for bullet in tanks_bullets:
        bullet[1] -= 5
        pygame.draw.circle(gameDisplay, COLORS["red"], (bullet[0]+10, bullet[1]), 5)
    tank_pos[0] = pygame.mouse.get_pos()[0]
    pygame.draw.rect(gameDisplay, COLORS["black"], (tank_pos[0], tank_pos[1], 20, 10))

    for bullet in tanks_bullets:
        for nlo in NLO:
            if nlo[0] < bullet[0] < nlo[0]+20 and nlo[1] < bullet[1] < nlo[1]+10:
                NLO.remove(nlo)
                tanks_bullets.remove(bullet)
                break
    

    if any(nlo[1]>height for nlo in NLO):
        print("Game Over!")
        run = False
        
    


# drawing code
   
    if randint(1, 10) > 8 and len(NLO)<10:
        NLO.append([randint(0, width-10), 20])
    pygame.display.update()
    clock.tick(FPS)


print("Thanks for playing!")
pygame.quit()

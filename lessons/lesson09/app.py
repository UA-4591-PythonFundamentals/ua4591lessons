import pygame


from colors import COLORS


pygame.init()


font = pygame.font.SysFont('Calibri', 25, True, False)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My Game')

clock = pygame.time.Clock()
FPS = 20
run = True
POINTS = []
current_pos = None
mouse_1_down = False
while run:

# event handling
    for event in pygame.event.get():
        # print(f"Event: {event}")
        match event.type:
            case pygame.QUIT:
                run = False
            case pygame.KEYDOWN:
                print(f"Key {event.key} pressed {event}")
            case pygame.KEYUP:
                print(f"Key {event.key} released {event}")
            case pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_1_down = True
                print(f"Mouse button {event.button} pressed at {event.pos}")
            case pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    mouse_1_down = False
                    if current_pos:
                        POINTS.append(current_pos)
                        current_pos = None
                elif event.button == 3:  # Right mouse button
                    if POINTS: POINTS.pop()
                print(f"Mouse button {event.button} released at {event.pos}")
            # case pygame.MOUSEMOTION:
            #     print(f"Mouse moved to {event.pos} with rel {event.rel} and buttons {event.buttons}")
            case _:
                pass
        if mouse_1_down:
            current_pos = pygame.mouse.get_pos()
    gameDisplay.fill(COLORS["white"])  # Fill the screen with white
# game logic
    print(f"Points: {POINTS}")

    if len(POINTS)>2:
        pygame.draw.polygon(gameDisplay, COLORS["blue"], POINTS)
    for point in POINTS:
        text_pos = font.render(f"{point}", True, COLORS["black"])
        gameDisplay.blit(text_pos, (point[0]-50, point[1]-30))

        pygame.draw.circle(gameDisplay, COLORS["red"], point, 5)
    
    if current_pos:
        text_pos = font.render(f"{current_pos}", True, COLORS["black"])
        gameDisplay.blit(text_pos, (current_pos[0]-50, current_pos[1]-30))
        pygame.draw.circle(gameDisplay, COLORS["green"], current_pos, 5)

# drawing code
   
    
    pygame.display.update()
    clock.tick(FPS)


print("Thanks for playing!")
pygame.quit()

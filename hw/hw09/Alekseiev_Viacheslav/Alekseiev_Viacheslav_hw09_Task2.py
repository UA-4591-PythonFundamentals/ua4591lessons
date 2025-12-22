import pygame


FPS = 60
WIDTH, HEIGHT = 500, 500


RECT_W, RECT_H = 40, 60
STEP = 5
x, y = 50, 50


BLACK = (0, 0, 0)
RED = (250, 0, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My first game")
clock = pygame.time.Clock()

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= STEP
    if keys[pygame.K_RIGHT]:
        x += STEP
    if keys[pygame.K_UP]:
        y -= STEP
    if keys[pygame.K_DOWN]:
        y += STEP

    
    x = max(0, min(x, WIDTH - RECT_W))
    y = max(0, min(y, HEIGHT - RECT_H))


    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (x, y, RECT_W, RECT_H))
    pygame.display.update()

    clock.tick(FPS)

pygame.quit()

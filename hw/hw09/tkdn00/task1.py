import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("Guess the number")

font = pygame.font.Font(None, 26)
question = "Guess the number between 1 and 100, you have 10 tries. Let`s goo!!!"
answer = ""
a = random.randint(1, 100)
n = 10
running = True

while running and n > 0:
    screen.fill((30, 30, 30))
    question_surface = font.render(question, True, (255, 255, 255))
    screen.blit(question_surface, (10,20))
    input_surface = font.render(f"Your answer: {answer}", True, (255, 255, 0))
    screen.blit(input_surface, (10, 80))
    attempts_surface = font.render(f"Your tries: {n}", True, (255, 255, 255))
    screen.blit(attempts_surface, (10, 60))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # print("Відповідь гравця:", answer)

                if answer == "" or not answer.isdigit():
                    error_text = font.render("It is not digit",True,(255, 255, 255))
                    screen.blit(error_text, (10,120))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    answer = ""
                    # n+=1
                    continue
                n -= 1
                if int(answer) == a:
                    guessed_text = font.render("Congratulations, you are winner!",True,(255, 255, 255))
                    screen.blit(guessed_text, (10, 120))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    answer = ""
                    running = False
                else:
                    if int(answer) > a:
                        too_high = font.render("Your guess is too high! Try again!", True, (255, 255, 255))
                        screen.blit(too_high, (10, 120))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        # print("Your guess is too high! Try again!")
                        answer = ""
                    elif int(answer) < a:
                        # print("Your guess is too low! Try again!")
                        too_low = font.render("Your guess is too low! Try again!", True, (255, 255, 255))
                        screen.blit(too_low, (10, 120))
                        pygame.display.update()
                        pygame.time.delay(1000)
                        answer = ""
            elif event.key == pygame.K_BACKSPACE:
                answer = answer[:-1]
            else:
                answer += event.unicode

    pygame.display.update()
if n == 0 and running:
    end_text = font.render("You are looser, try next time!", True, (255, 255, 0))
    screen.blit(end_text, (10, 180))
    pygame.display.update()
    pygame.time.delay(2000)


pygame.quit()


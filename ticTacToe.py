from turtle import circle
import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([600, 600])
running = True

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

while running:

    def drawCircle(coordinates):
        pygame.draw.circle(screen, black, coordinates, 75, 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] < 200 and mouse[0] > 000 and mouse[1] > 000 and mouse[1] < 200:
                print("1")
            if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 000 and mouse[1] < 200:
                print("2")
            if mouse[0] < 600 and mouse[0] > 400 and mouse[1] > 000 and mouse[1] < 200:
                print("3")
            if mouse[0] < 200 and mouse[0] > 000 and mouse[1] > 200 and mouse[1] < 400:
                print("4")
            if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 200 and mouse[1] < 400:
                print("5")
            if mouse[0] < 600 and mouse[0] > 400 and mouse[1] > 200 and mouse[1] < 400:
                print("6")
            if mouse[0] < 200 and mouse[0] > 000 and mouse[1] > 400 and mouse[1] < 600:
                print("7")
            if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 400 and mouse[1] < 600:
                print("8")
            if mouse[0] < 600 and mouse[0] > 400 and mouse[1] > 400 and mouse[1] < 600:
                print("9")
                drawCircle((500, 500))

    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()

    pygame.draw.line(screen, black, (0, 200), (600, 200), 1)
    pygame.draw.line(screen, black, (0, 400), (600, 400), 1)
    pygame.draw.line(screen, black, (200, 0), (200, 600), 1)
    pygame.draw.line(screen, black, (400, 0), (400, 600), 1)

    
    pygame.display.flip()

pygame.quit()
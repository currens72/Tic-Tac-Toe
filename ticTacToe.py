from turtle import circle
import pygame
pygame.init()

screen = pygame.display.set_mode([600, 600])
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 1)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 1)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 1)
    
    pygame.display.flip()

pygame.quit()
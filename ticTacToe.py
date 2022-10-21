from turtle import circle
import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([600, 600])
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 200 and mouse[1] < 400:
                print("Clicked")

    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()

    pygame.draw.line(screen, (0, 0, 0), (0, 200), (600, 200), 1)
    pygame.draw.line(screen, (0, 0, 0), (0, 400), (600, 400), 1)
    pygame.draw.line(screen, (0, 0, 0), (200, 0), (200, 600), 1)
    pygame.draw.line(screen, (0, 0, 0), (400, 0), (400, 600), 1)
    pygame.draw.rect(screen, (250, 0, 0), pygame.Rect(200, 200, 200, 200), 1)

    
    pygame.display.flip()

pygame.quit()
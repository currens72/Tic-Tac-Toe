from turtle import circle
import pygame
import ticTacToe

def beginMainMenu():
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode([200, 400])
    running = True

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    red = (255, 0, 0)

    gameFont = pygame.font.Font('freesansbold.ttf', 25)
    ticTacToe = gameFont.render('Tic-Tac-Toe', True, blue)
    hangman = gameFont.render('Hangman', True, blue)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[1] > 000 and mouse[1] < 75:
                    ticTacToe.runTicTacToe()
                if mouse[1] > 75 and mouse[1] < 150:
                    print("Hangman")

        screen.fill((255, 255, 255))
        mouse = pygame.mouse.get_pos()

        pygame.draw.line(screen, black, (0, 75), (200, 75), 1)
        pygame.draw.line(screen, black, (0, 150), (200, 150), 1)
        screen.blit(ticTacToe, (30, 25))
        screen.blit(hangman, (30, 100))
        
        pygame.display.update()

    pygame.quit()
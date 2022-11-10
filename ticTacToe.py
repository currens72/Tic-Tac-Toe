from turtle import circle
import pygame
import mainMenu

def runTicTacToe():
#    pygame.init()
#    pygame.font.init()

    tttScreen = pygame.display.set_mode([600, 650])
    running = True

    black = (0, 0, 0)
    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)
    red = (255, 0, 0)

    x = 2
    box1 = [0, 0, 0]
    box2 = [0, 0, 0]
    box3 = [0, 0, 0]
    box4 = [0, 0, 0]
    box5 = [0, 0, 0]
    box6 = [0, 0, 0]
    box7 = [0, 0, 0]
    box8 = [0, 0, 0]
    box9 = [0, 0, 0]

    resetFont = pygame.font.Font('freesansbold.ttf', 20)
    winFont = pygame.font.Font('freesansbold.ttf', 100)
    resetText = resetFont.render('Reset', True, red)
    xWinText = winFont.render('X Wins!', True, red)
    oWinText = winFont.render('O Wins!', True, red)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0] < 200 and mouse[0] > 000 and mouse[1] > 000 and mouse[1] < 200:
                    if box1[0] == 0:
                        box1 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 000 and mouse[1] < 200:
                    if box2[0] == 0:
                        box2 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 600 and mouse[0] > 400 and mouse[1] > 000 and mouse[1] < 200:
                    if box3[0] == 0:
                        box3 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 200 and mouse[0] > 000 and mouse[1] > 200 and mouse[1] < 400:
                    if box4[0] == 0:
                        box4 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 200 and mouse[1] < 400:
                    if box5[0] == 0:
                        box5 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 600 and mouse[0] > 400 and mouse[1] > 200 and mouse[1] < 400:
                    if box6[0] == 0:
                        box6 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 200 and mouse[0] > 000 and mouse[1] > 400 and mouse[1] < 600:
                    if box7[0] == 0:
                        box7 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 400 and mouse[0] > 200 and mouse[1] > 400 and mouse[1] < 600:
                    if box8[0] == 0:
                        box8 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 600 and mouse[0] > 400 and mouse[1] > 400 and mouse[1] < 600:
                    if box9[0] == 0:
                        box9 = [1, 1, x]
                        x = x + 1
                if mouse[0] < 350 and mouse[0] > 250 and mouse[1] > 610 and mouse[1] < 640:
                    x = 2
                    box1 = [0, 0, 0]
                    box2 = [0, 0, 0]
                    box3 = [0, 0, 0]
                    box4 = [0, 0, 0]
                    box5 = [0, 0, 0]
                    box6 = [0, 0, 0]
                    box7 = [0, 0, 0]
                    box8 = [0, 0, 0]
                    box9 = [0, 0, 0]

        tttScreen.fill((255, 255, 255))
        mouse = pygame.mouse.get_pos()

        pygame.draw.line(tttScreen, black, (0, 200), (600, 200), 1)
        pygame.draw.line(tttScreen, black, (0, 400), (600, 400), 1)
        pygame.draw.line(tttScreen, black, (200, 0), (200, 600), 1)
        pygame.draw.line(tttScreen, black, (400, 0), (400, 600), 1)
        pygame.draw.rect(tttScreen, red, pygame.Rect(250, 610, 100, 30), 1)
        tttScreen.blit(resetText, (275, 615))

        if box1[1] == 1:
            if box1[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (100, 100), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (25, 25), (175, 175))
                pygame.draw.line(tttScreen, black, (175, 25), (25, 175))
        if box2[1] == 1:
            if box2[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (300, 100), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (225, 25), (375, 175))
                pygame.draw.line(tttScreen, black, (375, 25), (225, 175))
        if box3[1] == 1:
            if box3[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (500, 100), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (425, 25), (575, 175))
                pygame.draw.line(tttScreen, black, (575, 25), (425, 175))
        if box4[1] == 1:
            if box4[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (100, 300), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (25, 225), (175, 375))
                pygame.draw.line(tttScreen, black, (175, 225), (25, 375))
        if box5[1] == 1:
            if box5[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (300, 300), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (225, 225), (375, 375))
                pygame.draw.line(tttScreen, black, (375, 225), (225, 375))
        if box6[1] == 1:
            if box6[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (500, 300), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (425, 225), (575, 375))
                pygame.draw.line(tttScreen, black, (575, 225), (425, 375))
        if box7[1] == 1:
            if box7[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (100, 500), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (25, 425), (175, 575))
                pygame.draw.line(tttScreen, black, (175, 425), (25, 575))
        if box8[1] == 1:
            if box8[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (300, 500), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (225, 425), (375, 575))
                pygame.draw.line(tttScreen, black, (375, 425), (225, 575))
        if box9[1] == 1:
            if box9[2] % 2 == 1:
                pygame.draw.circle(tttScreen, black, (500, 500), 75, 1)
            else:
                pygame.draw.line(tttScreen, black, (425, 425), (575, 575))
                pygame.draw.line(tttScreen, black, (575, 425), (425, 575))

        #HORIZONTAL WINS
        if box3[2] % 2 == box2[2] % 2 == box1[2] % 2 and box3[2] != 0 and box2[2] != 0 and box1[2] != 0 :
            if box3[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))
        if box6[2] % 2 == box5[2] % 2 == box4[2] % 2 and box6[2] != 0 and box5[2] != 0 and box4[2] != 0 :
            if box6[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))
        if box9[2] % 2 == box8[2] % 2 == box7[2] % 2 and box9[2] != 0 and box8[2] != 0 and box7[2] != 0 :
            if box9[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))

        #VERTICAL WINS
        if box1[2] % 2 == box4[2] % 2 == box7[2] % 2 and box1[2] != 0 and box4[2] != 0 and box7[2] != 0 :
            if box1[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))
        if box2[2] % 2 == box5[2] % 2 == box8[2] % 2 and box2[2] != 0 and box5[2] != 0 and box8[2] != 0 :
            if box2[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))
        if box3[2] % 2 == box6[2] % 2 == box9[2] % 2 and box3[2] != 0 and box6[2] != 0 and box9[2] != 0 :
            if box3[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))

        #DIAGONAL WINS
        if box1[2] % 2 == box5[2] % 2 == box9[2] % 2 and box1[2] != 0 and box5[2] != 0 and box9[2] != 0 :
            if box1[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))
        if box3[2] % 2 == box5[2] % 2 == box7[2] % 2 and box3[2] != 0 and box5[2] != 0 and box7[2] != 0 :
            if box3[2] % 2 == 1:
                tttScreen.blit(oWinText, (120, 250))
            else:
                tttScreen.blit(xWinText, (120, 250))
        
        pygame.display.update()

    pygame.quit()
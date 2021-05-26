import pygame
pygame.init()
from Grid import Grid

surface = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Tic Tac Toe')

#Icon
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

grid = Grid()
running = True
player = 'X'

#Player score position
score_X = 0
score_O = 0
text = pygame.font.SysFont('Arial Black', 15)

#Score Position
score_pos1_X = 350
score_pos1_Y = 40

score_pos2_X = 350
score_pos2_Y = 100

#Player font position
player1_X = 310
player1_Y = 20

player2_X = 310
player2_Y = 80

#Game Name
font = pygame.font.SysFont('Arial Black', 40)
nameX = 44
nameY = 320

def show_playerX(x, y):
    player1 = text.render('PLAYER X', True, (255, 255, 255))
    surface.blit(player1, (x, y))

def show_playerO(x, y):
    player2 = text.render('PLAYER Y', True, (255, 255, 255))
    surface.blit(player2, (x, y))

def show_scoreX(x, y):
    score1 = text.render(str(score_X), True, (255, 255, 255))
    surface.blit(score1, (x, y))

def show_scoreO(x, y):
    score2 = text.render(str(score_O), True, (255, 255, 255))
    surface.blit(score2, (x, y))

def game_name(x, y):
    name = font.render('TICK TAC TOE', True, (255, 255, 255))
    surface.blit(name, (x, y))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                grid.get_mouse(pos[0] // 100, pos[1] // 100, player)
                if grid.switch_player:
                    if player == 'X':
                        player = 'O'
                    else:
                        player = 'X'



    surface.fill((0, 0, 0))
    grid.draw(surface)
    show_playerX(player1_X, player1_Y)
    show_playerO(player2_X, player2_Y)
    show_scoreX(score_pos1_X, score_pos1_Y)
    show_scoreO(score_pos2_X, score_pos2_Y)
    game_name(nameX, nameY)

    pygame.display.flip()

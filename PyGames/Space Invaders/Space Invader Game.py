import pygame
import random
import math
from pygame import mixer

pygame.init()

# Create Screen
screen = pygame.display.set_mode((700, 650))
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load('rocket1.png')
playerX = 300
playerY = 550
playerX_change = 0

# Enemy
EnemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
total_enemies = 6
for i in range(total_enemies):
    EnemyImg.append(pygame.image.load('space-invader-icon.png'))
    enemyX.append(random.randint(0, 610))
    enemyY.append(random.randint(20, 100))
    enemyX_change.append(0.45)
    enemyY_change.append(30)

# Bullet
BulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 550
bulletX_change = 0
bulletY_change = 2
bullet_state = 'Steady'

# Background
background = pygame.image.load('tpqRdk.jpg')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 28)

textX = 10
textY = 10

# Player Identity
player_name = 1
player_positionX = 550
player_positionY = 10

# Game Over
game_over_font = pygame.font.Font('freesansbold.ttf', 50)
game_over_textX = 200
game_over_textY = 300

play_again = pygame.font.Font('freesansbold.ttf', 18)
playX = 240
playY = 350


def show_score(x, y):
    score = font.render('SCORE ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def show_player(x, y):
    player1 = font.render('PLAYER 1', True, (255, 255, 255))
    screen.blit(player1, (x, y))


def game_over(x, y):
    over_game = game_over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_game, (x, y))


def Play_Again(x, y):
    play_loop = play_again.render('Press Enter to play again', True, (255, 255, 255))
    screen.blit(play_loop, (x, y))


def player(x, y):
    screen.blit(PlayerImg, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'Fire'
    screen.blit(BulletImg, (x + 15, y + 3))


def Collision(x1, x2, y1, y2):
    distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game Loop
while True:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    show_player(player_positionX, player_positionY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 1.0
            if event.key == pygame.K_RIGHT:
                playerX_change += 1.0
            if event.key == pygame.K_SPACE:
                if bullet_state == 'Steady':
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 610:
        playerX = 610

    # Enemy Movement
    for i in range(total_enemies):
        # Game Over
        if enemyY[i] > 450:
            for j in range(total_enemies):
                enemyY[j] = 2000
            game_over(game_over_textX, game_over_textY)
            Play_Again(playX, playY)
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.45
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= 610:
            enemyX_change[i] = -0.45
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = Collision(enemyX[i], bulletX, enemyY[i], bulletY)
        if collision:
            collision_sound = mixer.Sound('explosion.wav')
            collision_sound.play()
            bulletY = 550
            bullet_state = 'Steady'
            score_value += 1
            enemyX[i] = random.randint(0, 610)
            enemyY[i] = random.randint(20, 100)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 550
        bullet_state = "Steady"

    if bullet_state == 'Fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)


import pygame

pygame.init()

# Create Screen
screen = pygame.display.set_mode((700,650))
pygame.display.set_caption('Connect the Dots')

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()


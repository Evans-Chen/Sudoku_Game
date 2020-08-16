import pygame

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.set_mode((
    WIDTH,
    HEIGHT)
)

pygame.display.set_caption("Space Invader")
icon = pygame.image.load(ufo.png)
pygame.display.set_icon(icon)

def player():

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False
    
    player()
    pygame.display.update()
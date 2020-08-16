import pygame
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 400
playerX_delta = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_delta = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_delta = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_delta = 0
    
    playerX += playerX_delta
    player(playerX % WIDTH, playerY)
    pygame.display.update()
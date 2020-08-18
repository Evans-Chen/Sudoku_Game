import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

# Display 
pygame.display.set_caption('Space Invader')
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Screen 
WINDOW_SIZE = (500, 600)
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)

# Player
player_image = pygame.image.load('player.png')
def player(location):
    screen.blit(player_image, location)


# enemyImg = pygame.image.load('enemy.png')
# enemyX = 370
# enemyY = 50
# enemyX_delta = 0
# def enemy(x, y):
#     screen.blit(enemyImg, (x, y))

moving_left = False
moving_right = False

player_location = [50, 50]
player_y_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(0, 200, 200, 50)

running = True
while running:
    screen.fill((146, 244, 255))
    player(player_location)

    # Momentum
    if player_location[1] > WINDOW_SIZE[1]-player_image.get_height():
        player_y_momentum = -player_y_momentum
    else:
        player_y_momentum += 0.2
    player_location[1] += player_y_momentum

    # Movement
    if moving_left:
        player_location[0] -= 4
    if moving_right:
        player_location[0] += 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]

    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen, (255, 0, 0), test_rect)
        player_y_momentum = -player_y_momentum
    else:
        pygame.draw.rect(screen, (0, 0, 0), test_rect)
    player_location[1] += player_y_momentum

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_RIGHT:
                moving_right = True
        if event.type == KEYUP:
            if event.key == K_LEFT:
                moving_left = False
            if event.key == K_RIGHT:
                moving_right = False
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
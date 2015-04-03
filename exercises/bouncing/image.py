import os
import pygame
import pygame.display

# Module to load images...
import pygame.image

import pygame.time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()


HERE = os.path.dirname(__file__)
ball = pygame.image.load(os.path.join(HERE, '..','images', 'ball.png'))
ball.convert(screen)
rect = ball.get_rect(center=(150, 150))

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            raise SystemExit(0)

    screen.fill((0, 0, 0))
    
    # copy our image to the screen at the given location (rectangle)
    screen.blit( ball, rect)
    
    pygame.display.flip()
    clock.tick(60)

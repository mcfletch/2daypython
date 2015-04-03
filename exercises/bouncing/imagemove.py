import os
import pygame
import pygame.display

screen = pygame.display.set_mode((300, 300))
pygame.display.init()


import pygame.image
HERE = os.path.dirname(__file__)
ball = pygame.image.load(os.path.join(HERE, '..','images', 'ball.png'))
ball.convert(screen)
rect = ball.get_rect(center=(150, 150))

# we need to track of our screen refreshes 
import pygame.time
clock = pygame.time.Clock()


while True:
    
    # note that now we pull out a *single* event at a time 
    # and we will pull out "NOEVENT" messages if we don't get any other message
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
        raise SystemExit(0)
    
    # What keys are currently being pressed?
    pressed = pygame.key.get_pressed()
    step = 2
    # Update our ball location based on what keys are being pressed...
    if pressed[pygame.K_UP]:
        rect.top = rect.top -step
        if rect.top < 0:
            rect.top = 0
    if pressed[pygame.K_DOWN]:
        rect.bottom = rect.bottom +step
        if rect.bottom > 300:
            rect.bottom = 300
    if pressed[pygame.K_LEFT]:
        rect.left = rect.left - step
        if rect.left < 0:
            rect.left = 0
    if pressed[pygame.K_RIGHT]:
        rect.right = rect.right + step
        if rect.right > 300:
            rect.right = 300

    screen.fill((0, 0, 0))
    screen.blit( ball, rect)
    pygame.display.flip()

    clock.tick(60)

import pygame
import pygame.display
import pygame.time

# tracks how long before the next frame of our animation...
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()

def process_events():
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            # was it the user asking to exit?
            raise SystemExit(0)
        # other event types handled here...
        event = pygame.event.poll()

import os
import pygame.image
HERE = os.path.dirname(__file__)
ball = pygame.image.load(os.path.join(HERE, '..','images', 'happyface.png'))
ball.convert(screen)
rectangle = ball.get_rect(center=(150, 150))

def render(screen, image, rectangle):
    # colour here is black, 0 red, 0 green, 0 blue
    screen.fill((0, 0, 0))
    
    # display the text...
    screen.blit( image, rectangle)
    
    pygame.display.flip()

while True:
    
    # did anything happen since the last screen-refresh?
    process_events()
    # display our new scene...
    render(screen, ball, rectangle)
    
    clock.tick(60)


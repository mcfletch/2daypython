import pygame
import pygame.display
import pygame.time
import pygame.sprite

class ImageSprite(pygame.sprite.Sprite):
    def __init__(self, image, rect=None):
        self.image =image
        self.rect = rect or image.get_rect()
        super(ImageSprite, self).__init__()

# tracks how long before the next frame of our animation...
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()

def process_events(ball):
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            # was it the user asking to exit?
            raise SystemExit(0)
        # other event types handled here...
        event = pygame.event.poll()
    # What keys are currently being pressed?
    pressed = pygame.key.get_pressed()
    
    step = 2
    rect = ball.rect
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

import os
import pygame.image
HERE = os.path.dirname(__file__)
ball = pygame.image.load(os.path.join(HERE, '..','images', 'happyface.png')).convert_alpha(screen)
girder = pygame.image.load(os.path.join(HERE, '..','images', 'girder-red.png')).convert(screen)

def bottom_platform(image):
    s_rect = screen.get_rect()
    rect = image.get_rect(bottomright=(0, 300))
    while rect.right < s_rect.right:
        girder = ImageSprite(image, image.get_rect(bottomleft=rect.bottomright ))
        all_sprites.add(girder)
        rect = girder.rect

ball = ImageSprite(ball, ball.get_rect(center=(150, 150)))
all_sprites = pygame.sprite.Group()
all_sprites.add(ball)

bottom_platform(girder)

def render(screen):
    # colour here is black, 0 red, 0 green, 0 blue
    screen.fill((250, 250, 250))
    
    # display the text...
    all_sprites.draw(screen)
    
    pygame.display.flip()

while True:
    
    # did anything happen since the last screen-refresh?
    process_events(ball)
    # display our new scene...
    render(screen)

    clock.tick(60)


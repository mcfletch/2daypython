import os
import pygame
import pygame.display
import pygame.image
import pygame.time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()

HERE = os.path.dirname(__file__)
ball = pygame.image.load(os.path.join(HERE, '..','images', 'ball.png'))
ball.convert(screen)
rect = ball.get_rect(center=(150, 150))

direction = (308/60., 157/60.)

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            raise SystemExit(0)

    distance = direction[0], direction[1]
    rect = rect.move((distance))
    
    if (rect.top < 0 or rect.bottom > 300) and (rect.left < 0 or rect.right > 300):
        direction = -direction[0], -direction[1]
    elif rect.top < 0 or rect.bottom > 300:
        direction = direction[0], -direction[1]
    elif rect.left < 0 or rect.right > 300:
        direction = -direction[0], direction[1]

    screen.fill((0, 0, 0))
    screen.blit( ball, rect)
    pygame.display.flip()
    
    clock.tick(60)

import pygame
import pygame.display
import pygame.time

# tracks how long before the next frame of our animation...
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()

while True:
    
    # did anything happen since the last screen-refresh?
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
        # was it the user asking to exit?
        raise SystemExit(0)

    # colour here is black, 0 red, 0 green, 0 blue
    screen.fill((0, 0, 0))
    pygame.display.flip()

    # do not render more than 60 times/second
    clock.tick(60)

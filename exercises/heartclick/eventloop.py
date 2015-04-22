# Multimedia library, display/screen control, timing control
import pygame
import pygame.display
import pygame.time
# What does our time-keeping for us... a clock
clock = pygame.time.Clock()
# Window 300x300 pixels, then make it visible
screen = pygame.display.set_mode((300, 300))
pygame.display.init()

while True:
    # process all the events since the last frame
    event = pygame.event.poll()
    # NOEVENT means "no more events"
    while not (event.type == pygame.NOEVENT): 
        if ( # was the user asking to exit?
            event.type == pygame.QUIT or
            (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        ):
            raise SystemExit(0)
        
        # get the next event to process
        event = pygame.event.poll()
    
    # display our new frame, the colour is a very light pink...
    screen.fill((255,230,230))
    pygame.display.flip()
    # wait the rest of the 1/60th of a second
    clock.tick(60)

# Multimedia library, display/screen control, timing control
import pygame
import pygame.display
import pygame.time
# What does our time-keeping for us... a clock
clock = pygame.time.Clock()
# Window 300x300 pixels, then make it visible
screen = pygame.display.set_mode((300, 300))
pygame.display.init()

# Here is where we will set up the game's images,
# sounds, and anything else we need to run...

while True:
    # Get the first waiting event from the user...
    event = pygame.event.poll()
    # NOEVENT means "no more events"
    while not (event.type == pygame.NOEVENT): 
        if ( # was the user asking to exit?
            event.type == pygame.QUIT or
            (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        ):
            raise SystemExit(0)
        
        # here is where we will process the user's mouse-clicks, keyboard
        # presses, etceteras
        
        # get the next event to process
        event = pygame.event.poll()
    
    # Display our frame, the colour is a very light pink...
    # (RED,GREEN,BLUE) with each value from 0 to 255
    screen.fill((255,230,230))
    
    # here is where we will draw the game...
    
    # Until now we've been drawing off-screen, now we'll "flip" 
    # the drawn surface onto the screen
    pygame.display.flip()
    # wait the rest of the 1/60th of a second
    clock.tick(60)

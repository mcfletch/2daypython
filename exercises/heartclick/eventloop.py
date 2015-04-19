import pygame
import pygame.display
import pygame.time

# creates a thing that does our time-keeping for us...
clock = pygame.time.Clock()

# sets the game-space to be 300 by 300 pixels
screen = pygame.display.set_mode((300, 300))
pygame.display.init()

while True:
    
    # Process all of the "things" (events) that have happened since the 
    # last time we drew a "frame"
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT):
        # was the user asking to exit?
        if (
            event.type == pygame.QUIT or
            (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        ):
            raise SystemExit(0)
        # Here is where we will handle the user's input
        # mouse-events, keyboard events, window-hide/show, etc.
        
        # get the next event to process
        event = pygame.event.poll()
    
    # display our new frame...
    # this colour is "black"
    screen.fill((0, 0, 0))
    
    # this is where we draw the our scene
    
    # show what we've drawn to the user
    pygame.display.flip()
    
    # ask the clock to wait the rest of the 1/60th of a second
    # so that we get approximately the right frame rate...
    clock.tick(60)

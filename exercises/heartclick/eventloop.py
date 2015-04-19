# We need a number of library functions...
# Multimedia library
import pygame
# Control the display/screen
import pygame.display
# Calculate/control timing...
import pygame.time

# A thing that does our time-keeping for us... a clock
clock = pygame.time.Clock()

# make the game's window 300 by 300 pixels
screen = pygame.display.set_mode((300, 300))
# then makes the screen show up...
pygame.display.init()

# Our same while-loop as in guessing game...
while True:
    
    # Process all of the "things" (events) that have happened since the 
    # last time we drew a "frame"
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT): # NOEVENT means "no more events"
        # was the user asking to exit?
        if (
            event.type == pygame.QUIT or
            (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        ):
            raise SystemExit(0)
        # Here is where we will handle the user's input
        # mouse-events, keyboard events, window-hide/show, etc.
        
        # get the next event to process (which may be NOEVENT)
        event = pygame.event.poll()
    
    # We have finished processing all of the updates from the user
    # (or the system, now let's show the game screen)
    
    # display our new frame...
    # this colour is a very light pink...
    screen.fill((255,230,230))
    
    # this is where we draw the our game
    
    # show what we've drawn to the user
    pygame.display.flip()
    
    # ask the clock to wait the rest of the 1/60th of a second
    # so that we get approximately the right frame rate...
    clock.tick(60)

import pygame
import pygame.display
import pygame.time

# creates a thing that does our time-keeping for us...
clock = pygame.time.Clock()

# sets the game-space to be 300 by 300 pixels
screen = pygame.display.set_mode((300, 300))
pygame.display.init()

#load_image_start
import os
import pygame.image
HERE = os.path.dirname(__file__)
heart = pygame.image.load(os.path.join(HERE,'heart.png'))
heart = heart.convert_alpha(screen)
heart_rectangle = heart.get_rect(center=(150, 150))
#load_image_stop
#load_award_start
award = pygame.image.load(os.path.join(HERE,'award.png'))
award = award.convert_alpha(screen)
#load_award_stop

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
        
        #click_check_start
        if event.type == pygame.MOUSEBUTTONDOWN:
            if heart_rectangle.collidepoint(event.pos):
                # the user won, yay!
                # Change the icon to an award
                heart = award
                #timer_exit_start
                # Quit 1.5s after they win
                pygame.time.set_timer(pygame.QUIT, 1500)
                #timer_exit_stop
        #click_check_stop
        
        # get the next event to process
        event = pygame.event.poll()
    
    # display our new frame...
    # this colour is "black"
    screen.fill((255,230,230))
    
    #draw_image_start
    # this is where we draw the our scene
    screen.blit( heart, heart_rectangle)
    #draw_image_stop
    
    # show what we've drawn to the user
    pygame.display.flip()
    
    # ask the clock to wait the rest of the 1/60th of a second
    # so that we get approximately the right frame rate...
    clock.tick(60)

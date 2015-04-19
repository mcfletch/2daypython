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
# __file__ is the filename of *this* python file
# os.path.dirname(filename) finds the directory that holds the filename
HERE = os.path.dirname(__file__)
# os.path.join( directory, 'name.png' ) gives us the file "next to" our 
# python file called "heart.png"
heart = pygame.image.load(os.path.join(HERE,'heart.png'))
heart = heart.convert_alpha(screen)
# where to display this image?
# we want to start the heart in the centre of the screen
# note the *american* spelling of "center", not Canadian/British spelling!
heart_rectangle = heart.get_rect(center=(150, 150))
#load_image_stop
#load_award_start
award = pygame.image.load(os.path.join(HERE,'award.png'))
award = award.convert_alpha(screen)
#load_award_stop

#motion_setup_start
import random
direction = (random.randint(-5,5),random.randint(-5,5))
#motion_setup_stop

#audio_prompts_start
import pygame.mixer
pygame.mixer.init()
instructions = pygame.mixer.Sound(os.path.join(HERE,'clicktowin.ogg'))
instructions.play()
congratulations = pygame.mixer.Sound(os.path.join(HERE,'youwin.ogg'))
#audio_prompts_stop

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
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if heart_rectangle.collidepoint(event.pos):
                # the user won, yay!
                heart = award
                direction = 0,0
                congratulations.play().set_endevent( pygame.QUIT )
        
        # get the next event to process
        event = pygame.event.poll()
    
    #update_motion_start
    heart_rectangle = heart_rectangle.move(direction)
    
    if (heart_rectangle.top < 0 or heart_rectangle.bottom > 300) and (heart_rectangle.left < 0 or heart_rectangle.right > 300):
        direction = -direction[0], -direction[1]
    elif heart_rectangle.top < 0 or heart_rectangle.bottom > 300:
        direction = direction[0], -direction[1]
    elif heart_rectangle.left < 0 or heart_rectangle.right > 300:
        direction = -direction[0], direction[1]
    
    # now a bit of randomness...
    if random.random() > .98:
        direction = direction[1],direction[0]
    #update_motion_stop
    
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

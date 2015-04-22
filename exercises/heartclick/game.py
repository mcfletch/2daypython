import pygame
import pygame.display
import pygame.time

# creates a thing that does our time-keeping for us...
clock = pygame.time.Clock()

# sets the game-space to be 300 by 300 pixels
screen = pygame.display.set_mode((300, 300))
pygame.display.init()

#find_image_start
import os
# __file__ is the filename of *this* python file
# os.path.dirname(filename) finds the directory that holds the filename
HERE = os.path.dirname(__file__)
# os.path.join( HERE, 'name.png' ) gives us the file "next to" our 
# python file called "heart.png"
heart_filename = os.path.join(HERE,'heart.png')
#find_image_stop
#load_image_start
import pygame.image
# Open this filename and interpret the contents as an image file
heart = pygame.image.load(heart_filename)
# Convert the image into a format that is appropriate for our screen
heart = heart.convert_alpha(screen)
# Where to display this image?
# we want to start the heart in the centre of the screen
# note the *American* spelling of "center", not Canadian/British spelling!
heart_rectangle = heart.get_rect(center=(150, 150))
#load_image_stop
#load_award_start
# Find, load and convert the user's award image...
award_filename = os.path.join(HERE,'award.png')
award = pygame.image.load(award_filename)
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
# start the instructions playing as soon as the game loads
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
        
        #click_check_start
        if event.type == pygame.MOUSEBUTTONDOWN:
            if heart_rectangle.collidepoint(event.pos):
        #click_check_stop
                #audio_award_start
                # the user won, yay!
                congratulations.play().set_endevent( pygame.QUIT )
                #audio_award_stop
                #show_award_start
                # The user has won, display their reward from now on!
                heart = award
                #show_award_stop
                direction = 0,0
        
        # get the next event to process
        event = pygame.event.poll()
    
    #bounce_start
    if heart_rectangle.top < 0 or heart_rectangle.bottom > 300:
        direction = direction[0], -direction[1]
    if heart_rectangle.left < 0 or heart_rectangle.right > 300:
        direction = -direction[0], direction[1]
    #bounce_stop
    
    #update_motion_start
    heart_rectangle.move(direction)
    #update_motion_stop
    
    #random_motion_start
    # now a bit of randomness...
    if random.random() > .98:
        direction = direction[1],direction[0]
    #random_motion_stop
    
    # display our new frame...
    # this colour is "black"
    screen.fill((255,230,230))
    
    #draw_image_start
    # this is where we draw our scene
    # "screen, please copy this image into this rectangle"
    screen.blit( heart, heart_rectangle)
    #draw_image_stop
    
    # show what we've drawn to the user
    pygame.display.flip()
    
    # ask the clock to wait the rest of the 1/60th of a second
    # so that we get approximately the right frame rate...
    clock.tick(60)

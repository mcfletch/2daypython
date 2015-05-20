import os
import pygame
import pygame.display
import pygame.time
import pygame.image
import random
import pygame.mixer

HERE = os.path.dirname(__file__)
# Note that the resources actually are *not* in the 
# same directory as the script in this case
RESOURCES = os.path.join( HERE, '..','heartclick' )

def setup_state(screen):
    """Setup the game to run on the given screen"""
    state = {}
    
    heart_filename = os.path.join(RESOURCES, 'heart.png')
    state['heart'] = pygame.image.load(heart_filename).convert_alpha(screen)
    state['heart_rectangle'] = state['heart'].get_rect(center=screen.get_rect().center)
    
    award_filename = os.path.join(RESOURCES,'award.png')
    state['award'] = pygame.image.load(award_filename).convert_alpha( screen )
    state['direction'] = (random.randint(-5,5),random.randint(-5,5))
    state['instructions'] = pygame.mixer.Sound(os.path.join(RESOURCES,'clicktowin.ogg'))
    # start the instructions playing as soon as the game loads
    state['congratulations'] = pygame.mixer.Sound(os.path.join(RESOURCES,'youwin.ogg'))
    
    # we explicitly choose which image to display...
    state['current_image'] = state['heart']
    return state

def check_user_input( state, event ):
    """Check for user input and update our game state"""
    if (
        event.type == pygame.QUIT or
        (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
    ):
        raise SystemExit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if state['heart_rectangle'].collidepoint(event.pos):
            channel = state['congratulations'].play()
            channel.set_endevent( pygame.QUIT )
            state['current_image'] = state['award']
            state['direction'] = (0,0)
    return state

def update_simulation( state, screen ):
    """Update our game's states based on simulation (time-based changes)
    
    screen is needed because we want to "bounce" at the edge of the screen
    """
    heart_rectangle = state['heart_rectangle']
    direction = state['direction']
    
    screen_rect = screen.get_rect()
    if heart_rectangle.top < 0 or heart_rectangle.bottom > screen_rect.bottom:
        direction = direction[0], -direction[1]
    if heart_rectangle.left < 0 or heart_rectangle.right > screen_rect.right:
        direction = -direction[0], direction[1]
    
    heart_rectangle = heart_rectangle.clamp( screen.get_rect())
    
    heart_rectangle = heart_rectangle.move(direction)
    
    if random.random() > .98:
        direction = direction[1],direction[0]
    
    # we have to update the state with the values we have calculated
    state['direction'] = direction
    state['heart_rectangle'] = heart_rectangle
    return state

def draw_game( state, screen ):
    """Draw our game's current state onto the given screen"""
    screen.fill((255,230,230))
    screen.blit( state['current_image'], state['heart_rectangle'])
    pygame.display.flip()

def main():
    """Main is the traditional name for the overall script function"""
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((640, 480))
    pygame.mixer.init()
    pygame.display.init()

    state = setup_state(screen)
    state['instructions'].play()

    while True:
        
        event = pygame.event.poll()
        while not (event.type == pygame.NOEVENT):
            state = check_user_input( state, event )
            event = pygame.event.poll()
        
        state = update_simulation( state, screen )
        draw_game(state,screen)
        clock.tick(60)

#main_call_start
# this stanza reads as "if we are the main script, run function main"
if __name__ == "__main__":
    main()
#main_call_stop
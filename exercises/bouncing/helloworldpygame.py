import pygame
import pygame.display
import pygame.time

# tracks how long before the next frame of our animation...
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()

def process_events():
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            # was it the user asking to exit?
            raise SystemExit(0)
        # other event types handled here...
        event = pygame.event.poll()

# fonts are descriptions of how to render text as images
import pygame.font
# we need to initialize the font engine...
pygame.font.init()
# now we'll get the default system font name
font_name = pygame.font.get_default_font()
# and we'll request a version of it that renders 32 pixels high
font = pygame.font.Font(font_name, 32)
# now we create an image from our text and the font...
text = font.render("Hello, World!", True, (255, 255, 255), )
rectangle = text.get_rect(center=(150, 150))

def render(screen, text, rectangle):
    # colour here is black, 0 red, 0 green, 0 blue
    screen.fill((0, 0, 0))
    
    # display the text...
    screen.blit( text, rectangle)
    
    pygame.display.flip()

while True:
    
    # did anything happen since the last screen-refresh?
    process_events()
    # display our new scene...
    render(screen, text, rectangle)
    
    clock.tick(60)

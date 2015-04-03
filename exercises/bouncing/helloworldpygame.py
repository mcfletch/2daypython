import pygame
import pygame.display
import pygame.time
clock = pygame.time.Clock()

screen = pygame.display.set_mode((300, 300))
pygame.display.init()

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

while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
        raise SystemExit(0)

    screen.fill((0, 0, 0))
    
    # we copy the text to the screen every refresh
    screen.blit( text, rectangle)
    
    pygame.display.flip()
    clock.tick(60)

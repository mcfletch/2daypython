import pygame
import pygame.display
import pygame.time
import pygame.font
import sys

clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))

pygame.font.init()
pygame.display.init()

font_name = pygame.font.get_default_font()
font = pygame.font.Font(font_name, 32)
text = font.render("Hello, World! %s.%s"%sys.version_info[:2], True, (255, 255, 255), )
rectangle = text.get_rect(center=(150, 150))

def process_events():
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT):
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            raise SystemExit(0)
        event = pygame.event.poll()

def render(screen, text, rectangle):
    screen.fill((0, 0, 0))
    screen.blit( text, rectangle)
    pygame.display.flip()

while True:
    process_events()
    render(screen, text, rectangle)
    
    clock.tick(60)

# Game Setup
import pygame
import pygame.display
import pygame.time
clock = pygame.time.Clock()
screen = pygame.display.set_mode((300, 300))
pygame.display.init()
import os
HERE = os.path.dirname(__file__)
heart_filename = os.path.join(HERE,'heart.png')
import pygame.image
heart = pygame.image.load(heart_filename)
heart = heart.convert_alpha(screen)
heart_rectangle = heart.get_rect(center=(150, 150))
award_filename = os.path.join(HERE,'award.png')
award = pygame.image.load(award_filename)
award = award.convert_alpha(screen)
import random
direction = (random.randint(-5,5),random.randint(-5,5))
import pygame.mixer
pygame.mixer.init()
instructions = pygame.mixer.Sound(os.path.join(HERE,'clicktowin.ogg'))
instructions.play()
congratulations = pygame.mixer.Sound(os.path.join(HERE,'youwin.ogg'))

# Rendering Loop
while True:
    
    # Event Loop
    event = pygame.event.poll()
    while not (event.type == pygame.NOEVENT):
        if (
            event.type == pygame.QUIT or
            (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE)
        ):
            raise SystemExit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if heart_rectangle.collidepoint(event.pos):
                congratulations.play().set_endevent( pygame.QUIT )
                # modifying the model here...
                heart = award
                direction = 0,0
        event = pygame.event.poll()
    
    # Update the Game Simulation
    if heart_rectangle.top < 0 or heart_rectangle.bottom > 300:
        direction = direction[0], -direction[1]
    if heart_rectangle.left < 0 or heart_rectangle.right > 300:
        direction = -direction[0], direction[1]
    heart_rectangle = heart_rectangle.move(direction)
    if random.random() > .98:
        direction = direction[1],direction[0]
    
    # Rendering
    screen.fill((255,230,230))
    screen.blit( heart, heart_rectangle)
    pygame.display.flip()
    clock.tick(60)

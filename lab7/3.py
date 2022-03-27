import pygame

pygame.init()                                                    # initialize all configs

screen = pygame.display.set_mode((1000, 700))                     # Creating main window (surface)

clock = pygame.time.Clock()
FPS = 60                                                         # Frame per second

running = True
x, y = 25, 25                                                    # starting point if circle
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:                            # pygame.QUIT - end point
            running = False


    pressed = pygame.key.get_pressed()                           # getting all pressed buttons
    if pressed[pygame.K_UP] and y - 20 >= 0:
        y -= 20
    if pressed[pygame.K_DOWN] and y + 20 <= 700:
        y += 20
    if pressed[pygame.K_RIGHT] and x + 20 <= 1000:
        x += 20
    if pressed[pygame.K_LEFT] and x - 20 >= 0:
        x -= 20
    
    screen.fill((255, 255, 255))                                 # refresh the screen

    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)          # drawing the circle 

    pygame.display.flip()                                        # screen updating

    clock.tick(FPS)

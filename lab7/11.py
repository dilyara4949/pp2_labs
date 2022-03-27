import pygame
import datetime
from math import pi, sin, cos

pygame.init()

width, height = 300, 300
run = True
center = (width / 2, height / 2)


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 60

image = pygame.image.load('f936c5a35c35c3f4d7c498fb8edad0f1.png')
im_sec = pygame.image.load('kindpng_129713.jpeg')

def pos(r, angle):
    x = r * sin(pi * angle/180)
    y = r * cos(pi*angle/180)
    return x + center[0], -(y - center[1]) 

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    time = datetime.datetime.now()
    second = time.second
    minute = time.minute


    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))

    # second hand
    r = 130
    angle = second * (360/60)
    pygame.draw.line(screen, (0, 0, 0), center,  pos(r, angle), 4)

    # minute hand
    r = 100
    angle = (minute + second/60) * (360/60)
    pygame.draw.line(screen, (0, 0, 0), center, pos(r, angle), 4)
    
    pygame.display.flip()

    clock.tick(FPS)
    
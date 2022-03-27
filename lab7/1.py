import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))

image = pygame.image.load('f936c5a35c35c3f4d7c498fb8edad0f1.png')
arrow = pygame.image.load('kindpng_129713.png')

running = True

ang = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    screen.blit(image, (0, 0))
    screen.blit(arrow, (0, 0))

# n_arrow = arrow.resize(())
    



    pygame.display.flip()
    



    # def rot_center(image, angle, x, y):
    
    # rotated_image = pygame.transform.rotate(image, angle)
    # new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    # return rotated_image, new_rect
print(arrow.size())
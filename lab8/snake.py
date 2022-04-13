import pygame
import random

pygame.init()

eaten_food = 0
speed = 4
level = 1

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

radius = 10
body = [[100, 100], [0, 0], [0, 0]]

block = 15
dx, dy = block, 0 

def own_round(value, base  = 15):
    return base * round(value / 15)
def set_random_position():
    return own_round(random.randint(0, WINDOW_WIDTH)), own_round(random.randint(0, WINDOW_HEIGHT))


game_over = False
food_x, food_y = None, None 

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:        
            if event.key == pygame.K_RIGHT:
                dx = block
                dy = 0
            if event.key == pygame.K_UP:
                dx = 0
                dy = -block
            if event.key == pygame.K_LEFT:
                dx = -block
                dy = 0
            if event.key == pygame.K_DOWN:
                dx = 0
                dy = block
            if event.key == pygame.K_t:
                ok = True
                while ok:
                    food_x , food_y = set_random_position()
                    for i in range(3):                                      # not to fall to a snake
                        a, b = (food_x, food_y, 10), (body[i][0], body[i][1], 10)
                        distance = ((a[0] - b[0])**2 + (a[1] - b[1])**2)
                        if distance == 0 or distance < (a[2] + b[2])**2:
                            break
                        elif i == 2 and distance != 0 and distance > (a[2] + b[2])**2:
                            ok = False
                        

    screen.fill(BLACK)
                   
    
    
    for i in range(len(body) - 1, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1]= body[i - 1][1]
    
    body[0][0] += dx
    body[0][1] +=dy

    if body[0][0] > 500:                    # not to leave boundaries
        body[0][0] = 0
    if body[0][0] < 0:
        body[0][0] = 500
    if body[0][1] > 500:
        body[0][1] = 0
    if body[0][1] < 0:
        body[0][1] = 500


    if food_x:
        pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)   # draw food


                                                    
    for i, (x, y) in enumerate(body):           #drawing snake
        color = RED if i == 0 else GREEN
        pygame.draw.circle(screen, color, (x, y), radius)

    
    if food_x:                                                      # calculating speed and level
        a, b = (food_x, food_y, 10), (body[0][0], body[0][1], 10)
        distance = ((a[0] - b[0])**2 + (a[1] - b[1])**2)
        if distance == 0 or distance < (a[2] + b[2])**2:
            pygame.draw.circle(screen, BLACK, (food_x, food_y), radius)
            food_x , food_y = set_random_position()
            pygame.draw.circle(screen, BLUE, (food_x, food_y), radius)
            eaten_food += 1
            if eaten_food % 3 == 0:
                speed += 3
                level += 1

    
    font = pygame.font.SysFont('Arial', 32)                # blit text  (level)
    img = font.render(f'level : {level}', True, (120, 100, 140))
    screen.blit(img, (10, 10))
    
    font = pygame.font.SysFont('Arial', 32)                # blit text  (level)
    img = font.render(f'score : {eaten_food}', True, (120, 100, 140))
    screen.blit(img, (10, 35))

    pygame.display.flip()

    clock.tick(speed)

pygame.quit()
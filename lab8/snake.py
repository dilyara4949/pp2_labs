import pygame
import random

pygame.init()


# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# other varibles
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
eaten_food = 0
speed = 4
level = 1
radius = 10
block = 15
dx, dy = block, 0
clock = pygame.time.Clock() 

# creating screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# body for snake
body = [[100, 100], [0, 0], [0, 0]]

# food_x, food_y = None, None 

# set randon pisition for food 
foodx = round(random.randrange(0, WINDOW_WIDTH - block) / 10.0) * 10.0
foody = round(random.randrange(0, WINDOW_HEIGHT - block) / 10.0) * 10.0

game_over = False

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
            
                        

    screen.fill(BLACK)            
    
    # moving the snake
    for i in range(len(body) - 1, 0, -1):
        body[i][0] = body[i - 1][0]
        body[i][1]= body[i - 1][1]
    body[0][0] += dx
    body[0][1] +=dy

    # not to leave boundaries
    if body[0][0] > 500:                    
        body[0][0] = 0
    if body[0][0] < 0:
        body[0][0] = 500
    if body[0][1] > 500:
        body[0][1] = 0
    if body[0][1] < 0:
        body[0][1] = 500

    

    # draw food
    pygame.draw.circle(screen, BLUE, [foodx, foody], radius)


    # drawing snake                                              
    for i, (x, y) in enumerate(body):           
        color = RED if i == 0 else GREEN
        pygame.draw.circle(screen, color, (x, y), radius)

   
    

    # calculating speed and level and eat food 
    a, b = (foodx, foody, 10), (body[0][0], body[0][1], 10)
    distance = ((a[0] - b[0])**2 + (a[1] - b[1])**2)
    if distance == 0 or distance < (a[2] + b[2])**2:
        pygame.draw.circle(screen, BLACK, (foodx, foody), radius)
        foodx = round(random.randrange(0, WINDOW_WIDTH - block) / 10.0) * 10.0
        foody = round(random.randrange(0, WINDOW_HEIGHT - block) / 10.0) * 10.0
        pygame.draw.circle(screen, BLUE, (foodx, foody), radius)
        eaten_food += 1
        if eaten_food % 3 == 0:
            speed += 3
            level += 1


    # blit text  (level)
    font = pygame.font.SysFont('Arial', 32)                
    img = font.render(f'level : {level}', True, (120, 100, 140))
    screen.blit(img, (10, 10))
    
    # blit text  (score)
    font = pygame.font.SysFont('Arial', 32)                
    img = font.render(f'score : {eaten_food}', True, (120, 100, 140))
    screen.blit(img, (10, 35))

    pygame.display.update()

    clock.tick(speed)

pygame.quit()
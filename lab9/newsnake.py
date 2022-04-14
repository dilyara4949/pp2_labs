import pygame, random

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
block = 15
clock = pygame.time.Clock() 

# creating screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


# body for snake
body = [[100, 100], [0, 0], [0, 0]]

class Food:
    def __init__(self):
        self.x = round(random.randrange(0, WINDOW_WIDTH - block) / 10.0) * 10.0
        self.y = round(random.randrange(0, WINDOW_HEIGHT - block) / 10.0) * 10.0
        self.radius = random.randint(10, 40)

    def draw(self):
        pygame.draw.circle(screen, BLUE, [self.x, self.y], self.radius)
            
    def redraw(self):
        self.x = round(random.randrange(0, WINDOW_WIDTH - block) / 10.0) * 10.0
        self.y = round(random.randrange(0, WINDOW_HEIGHT - block) / 10.0) * 10.0
        self.radius = random.randint(10, 40)

class Snake(Food):
    def __init__(self):
        super().__init__()
        self.block = 15
        self.dx = self.block
        self.dy = 0
        self.body = [[100, 100], [0, 0], [0, 0]]
    def move(self):
        for event in events:
            if event.type == pygame.KEYDOWN:        
                if event.key == pygame.K_RIGHT:
                    self.dx = self.block
                    self.dy = 0
                if event.key == pygame.K_UP:
                    self.dx = 0
                    self.dy = -self.block
                if event.key == pygame.K_LEFT:
                    self.dx = -self.block
                    self.dy = 0
                if event.key == pygame.K_DOWN:
                    self.dx = 0
                    self.dy = self.block
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1]= self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

        self.body[0][0] %= WINDOW_WIDTH
        self.body[0][1] %= WINDOW_HEIGHT

    def draw(self):
        for i, (x, y) in enumerate(self.body):           
            color = RED if i == 0 else GREEN
            pygame.draw.circle(screen, color, (x, y), 10)
        

            
    def eat_food(self, f:Food):
        global eaten_food, speed, level
        a, b = (f.x, f.y, 10), (self.body[0][0], self.body[0][1], f.radius)
        distance = ((a[0] - b[0])**2 + (a[1] - b[1])**2)
        if distance == 0 or distance < (a[2] + b[2])**2:
            f.redraw()
            eaten_food += 1
            if eaten_food % 3 == 0 and eaten_food > 1:
                speed += 3
                level += 1
                self.body[0][0] = 100      # returns to the start point
                self.body[0][1] = 100
                self.dx = self.block
                self.dy = 0

s = Snake()
f = Food()

time_delay = 12000
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)

game_over = False

while not game_over:
    clock.tick(speed)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            game_over = True
        # every 12 sec food will be redrawn
        if event.type == timer_event:      
            f.redraw()

    screen.fill(BLACK)            
    
    s.draw()
    s.move()
        
    f.draw()
    s.eat_food(f)


    # blit text  (level)
    font = pygame.font.SysFont('Arial', 32)                
    img = font.render(f'level : {level}', True, (120, 100, 140))
    screen.blit(img, (10, 10))
    
    # blit text  (score)
    font = pygame.font.SysFont('Arial', 32)                
    img = font.render(f'score : {eaten_food}', True, (120, 100, 140))
    screen.blit(img, (10, 35))

    pygame.display.update()
pygame.quit()
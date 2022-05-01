from random import randrange
import psycopg2, pygame, random, time

username = input('Enter your name...\n')
conn = psycopg2.connect(  
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
)

cursor = conn.cursor()
cursor.execute('SELECT * FROM snake WHERE username = %s;', [username])
data = cursor.fetchone()

if data == None:
    cursor.execute('INSERT INTO snake VALUES(%s, 0, 0, 0);', [username])
    conn.commit()

pygame.init()
FPS = 3
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


WIDTH, HEIGHT = 500, 500
block = 20
highscore = 0
level = 0

font = pygame.font.SysFont("Verdana", 20, False)
font1 = pygame.font.SysFont("Verdana", 30, False)

screen = pygame.display.set_mode((WIDTH, HEIGHT))


running = True

class Food:
    def __init__(self):
        self.x = randrange(0, WIDTH, block)
        self.y = randrange(0, HEIGHT, block)
   
    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, block, block)) 
    
    def redraw(self):
        self.x = randrange(0, WIDTH, block)
        self.y = randrange(0, HEIGHT, block)
    

class Wall:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, block, block))

class Snake:
    def __init__(self):
        self.score = 0
        self.body = [[40, 40],[0, 0],[0, 0]]
        self.dx = block
        self.dy = 0
        self.destination = ''
        self.color = BLUE
    
    def move(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.destination != 'right':
                    self.dx = -block
                    self.dy = 0
                    self.destination = 'left'
                if event.key == pygame.K_RIGHT and self.destination != 'left':
                    self.dx = block
                    self.dy = 0
                    self.destination = 'right'
                if event.key == pygame.K_UP and self.destination != 'down':
                    self.dx = 0
                    self.dy = -block
                    self.destination = 'up'
                if event.key == pygame.K_DOWN and self.destination != 'up':
                    self.dx = 0
                    self.dy = block
                    self.destination = 'down'
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i][0] = self.body[i - 1][0]
            self.body[i][1] = self.body[i - 1][1]

        self.body[0][0] += self.dx
        self.body[0][1] += self.dy

       
        self.body[0][0] %= WIDTH
        self.body[0][1] %= HEIGHT

    def draw(self):
        for i, (x, y) in enumerate(self.body):           
            color = (105, 105, 255) if i == 0 else BLUE
            pygame.draw.circle(screen, color, (x, y), 10)
        

    def collide_food(self, f:Food):
        if self.body[0][0] == f.x and self.body[0][1] == f.y:
            self.score += 2
           

    def collide_self(self):
        global running
        if self.body[0] in self.body[1:]:
            running = False
    def check_food(self, f:Food):
        if [f.x, f.y] in self.body:
            f.redraw()


s = Snake()
f = Food()


time_delay = 15000
timer_event = pygame.USEREVENT + 1 
pygame.time.set_timer(timer_event, time_delay)

while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == timer_event:
            f.redraw()
        if event.type == pygame.MOUSEBUTTONDOWN:
           if pygame.mouse.get_pos()[0] >= 440 and pygame.mouse.get_pos()[0] <= 480 and pygame.mouse.get_pos()[1] >= 20 and pygame.mouse.get_pos()[1] <= 60:
                screen.fill(RED)
                screen.blit(score, (150, 200))
                pygame.display.update()
                time.sleep(4)  

    screen.fill(WHITE)
    if s.score >= 3:
        level = 1
        FPS = 5
    if s.score >= 6:
        level = 2
        FPS = 5
    if s.score >= 9:
        level = 3
        FPS = 6
    if s.score >= 12:
        level = 4
        FPS = 7
    if s.score >= 15:
        level = 5
        FPS = 7
    walls_coor=  open(f'wall{level}.txt', 'r').readlines()
    
    walls = []

    for i, line in enumerate(walls_coor):
        for j, each in enumerate(line):
            if each == "#":
                walls.append(Wall(j * block, i * block))
    for wall in walls:
        wall.draw()
        if f.x == wall.x and f.y == wall.y:
            f.redraw()
        if s.body[0][0] == wall.x and s.body[0][1] == wall.y:
             screen.fill(RED)
             screen.blit(score, (150, 200))
             pygame.display.update()
             time.sleep(3)
             running = False

    f.draw()
    s.draw()
    s.move(events)
    s.collide_food(f)
    s.collide_self()
    s.check_food(f)
    
    pygame.draw.rect(screen, GREEN, (440, 20, 40, 40))
    score = font1.render(f'Your score: {s.score}', True, BLACK)
    text = font.render(f"Score: {s.score}", True, BLACK)
    text2 = font.render(f"Level: {level}", True, BLACK)
    screen.blit(text, (5, 0))
    screen.blit(text2, (5, 30))
    pygame.display.flip()
    f_score = s.score
pygame.quit()

if f_score > highscore:
    highscore = f_score

highscore = str(highscore)
f_score = str(f_score)
level = str(level)
sql = 'UPDATE snake SET user_score = %s, highscore = %s, level = %s WHERE username = %s;'
cursor.execute(sql, [f_score, highscore, level, username])
conn.commit()
cursor.close()
conn.close()
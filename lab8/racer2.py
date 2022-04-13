import pygame, time
import random
from pygame.locals import *

# initializing
pygame.init()

# colors 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# setting up FPS
FPS = 60
clock = pygame.time.Clock()

# other variables
WIDTH = 400
HEIGHT = 600
speed = 6
score = 0
picked_coins = 0

# setting up Fonts
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, BLACK)

background = pygame.image.load('road.png')


# create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Racer')

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Police.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Audi.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = random.randint(10, 15)
        self.x = random.randint(20, WIDTH - 20)
        self.y = -100
        self.image = pygame.transform.scale(pygame.image.load("Gold_1.png"), (25,25))
        self.surf = pygame.Surface((25,25), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(center = (self.x, self.y))
    
    def move(self):
        self.rect.move_ip(0, self.speed)
    
    def draw(self):
        self.surf.blit(self.image, (0,0))
        screen.blit(self.surf, self.rect)
    
    def kil(self):
        if self.rect.top > HEIGHT:
            self.kill()

    


# setting up sprites
P = Player()
E = Enemy()
C = Coin()

# creating sprites groups
coins = pygame.sprite.Group()
coins.add(C)
enemies = pygame.sprite.Group()
enemies.add(E)
all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)
# all_sprites.add(C)



# adding a new User event
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

song = '/Users/dilaramuhambetova/pp2_labs/lab8/background.wav'
pygame.mixer.Sound(song).play(-1)

run = True 

while run:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.2
        if event.type == pygame.QUIT:
            run = False
    

    screen.blit(background, (0, 0))
    scores = font_small.render(f'SCORE : {score}', True, BLACK)
    screen.blit(scores, (10,10))
    coinn = font_small.render(f'COIN : {picked_coins}', True, BLACK)
    screen.blit(coinn, (10, 29) )

    # moves and re_draws all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    if len(coins) < 2:
        coins.add(Coin())
    
        
    for coin in coins:
        coin.draw()
        coin.move()
        coin.kil()
    
    for coin in coins:
        if pygame.sprite.collide_rect(P, coin):
            coin.kill()
            picked_coins += 1
            coins.add(Coin())
    
   

    
    # to be run if collision occurs between playerand enemy 
    if pygame.sprite.spritecollideany(P, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30,250))
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        run = False   

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
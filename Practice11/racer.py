import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY  = (84, 79, 78)
YELLOW= (255, 215, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

SPEED = 5           
ENEMY_SPEED = 5       
COINS_COLLECTED = 0
N_COINS_TARGET = 10   

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font.render("Game Over", True, BLACK)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('C:/Users/Roar/Documents/GitHub/PP2/Practice10/img/Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, ENEMY_SPEED)

        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load('C:/Users/Roar/Documents/GitHub/PP2/Practice10/img/Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520) 
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.base_image = pygame.image.load('C:/Users/Roar/Documents/GitHub/PP2/Practice10/img/coin.png')
        self.reset_coin()

    def reset_coin(self):
        self.weight = random.choice([1, 3, 5])
        
        original_width = self.base_image.get_width()
        original_height = self.base_image.get_height()
        scale_factor = 1 + (self.weight * 0.1) 
        
        self.image = pygame.transform.scale(
            self.base_image, 
            (int(original_width * scale_factor), int(original_height * scale_factor))
        )

        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset_coin()


P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

while True:     
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.fill(GRAY)

    coin_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    collected_coins = pygame.sprite.spritecollide(P1, coins, False)
    for coin in collected_coins:
        previous_score = COINS_COLLECTED
        COINS_COLLECTED += coin.weight
        
        if (COINS_COLLECTED // N_COINS_TARGET) > (previous_score // N_COINS_TARGET):
            ENEMY_SPEED += 1
            
        coin.reset_coin()

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:/Users/Roar/Documents/GitHub/PP2/Practice10/crash.mp3').play() 
        time.sleep(0.5)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill() 
            
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    pygame.display.update()
    FramePerSec.tick(FPS)
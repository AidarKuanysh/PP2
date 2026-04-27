import pygame
import random
import time

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 215, 0)
CYAN = (0, 255, 255)
WHITE = (255,255,255)
MAGENTA = (255, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self, color_name):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        color = BLUE if color_name == "Blue" else RED if color_name == "Red" else GREEN
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        self.shield_active = False
        self.nitro_active = False
        self.powerup_end_time = 0

    def update_powerups(self):
        if time.time() > self.powerup_end_time:
            self.shield_active = False
            self.nitro_active = False

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        speed = 8 if self.nitro_active else 5
        if self.rect.left > 0 and pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-speed, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(speed, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((40, 70))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Coin(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.weight = random.choice([1, 3, 5])
        size = 20 + (self.weight * 2)
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (size//2, size//2), size//2)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class Hazard(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.image = pygame.Surface((50, 20))
        self.image.fill((139, 69, 19)) # Brown pothole
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(50, SCREEN_WIDTH - 50), -50)
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.type = random.choice(["Nitro", "Shield", "Repair"])
        self.image = pygame.Surface((30, 30))
        color = CYAN if self.type == "Shield" else MAGENTA if self.type == "Nitro" else GREEN
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
        self.speed = speed

    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

def run_game(screen, font, small_font, username, settings):
    clock = pygame.time.Clock()
    FPS = 60

    base_speed = 5 if settings["difficulty"] == "Easy" else 7 if settings["difficulty"] == "Normal" else 10
    world_speed = base_speed
    
    P1 = Player(settings["car_color"])
    enemies = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    hazards = pygame.sprite.Group()
    powerups = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group(P1)

    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, 1000)
    
    SPAWN_COIN = pygame.USEREVENT + 2
    pygame.time.set_timer(SPAWN_COIN, 1500)

    SPAWN_HAZARD = pygame.USEREVENT + 3
    pygame.time.set_timer(SPAWN_HAZARD, 3000)

    SPAWN_POWERUP = pygame.USEREVENT + 4
    pygame.time.set_timer(SPAWN_POWERUP, 8000)

    score = 0
    distance = 0.0
    lives = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return score, int(distance), False

            if event.type == SPAWN_ENEMY:
                new_enemy = Enemy(world_speed + random.randint(0, 2))
                if not pygame.sprite.spritecollideany(new_enemy, hazards):
                    enemies.add(new_enemy)
                    all_sprites.add(new_enemy)
            if event.type == SPAWN_COIN:
                new_coin = Coin(world_speed)
                coins.add(new_coin)
                all_sprites.add(new_coin)
            if event.type == SPAWN_HAZARD:
                new_hazard = Hazard(world_speed)
                hazards.add(new_hazard)
                all_sprites.add(new_hazard)
            if event.type == SPAWN_POWERUP:
                new_powerup = PowerUp(world_speed)
                powerups.add(new_powerup)
                all_sprites.add(new_powerup)

        P1.update_powerups()

        distance += (world_speed / 10)
        current_speed_mult = 1 + (distance // 500) * 0.1
        world_speed = int(base_speed * current_speed_mult)

        screen.fill((84, 79, 78))

        for entity in all_sprites:
            entity.move()
            screen.blit(entity.image, entity.rect)

        collected = pygame.sprite.spritecollide(P1, coins, True)
        for c in collected:
            score += c.weight * 10

        pwrs = pygame.sprite.spritecollide(P1, powerups, True)
        for p in pwrs:
            if p.type == "Nitro":
                P1.nitro_active = True
                P1.powerup_end_time = time.time() + 4
            elif p.type == "Shield":
                P1.shield_active = True
                P1.powerup_end_time = time.time() + 5
            elif p.type == "Repair":
                lives = 2 # Max lives

        if pygame.sprite.spritecollideany(P1, hazards):
            if P1.shield_active:
                pygame.sprite.spritecollide(P1, hazards, True)
                P1.shield_active = False
            else:
                world_speed = max(3, world_speed - 2)
                score = max(0, score - 20)
                pygame.sprite.spritecollide(P1, hazards, True)

        if pygame.sprite.spritecollideany(P1, enemies):
            if P1.shield_active:
                pygame.sprite.spritecollide(P1, enemies, True)
                P1.shield_active = False
            elif lives > 1:
                pygame.sprite.spritecollide(P1, enemies, True)
                lives -= 1
            else:
                if settings["sound"]:
                    pass
                screen.fill(RED)
                game_over_text = font.render("GAME OVER", True, BLACK)
                screen.blit(game_over_text, (50, 250))
                pygame.display.update()
                time.sleep(2)
                return score, int(distance), True

        dist_text = small_font.render(f"Dist: {int(distance)}m", True, WHITE)
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        screen.blit(dist_text, (10, 10))
        screen.blit(score_text, (10, 30))

        if P1.nitro_active:
            n_text = small_font.render("NITRO ACTIVE", True, MAGENTA)
            screen.blit(n_text, (10, 50))
        if P1.shield_active:
            s_text = small_font.render("SHIELD ACTIVE", True, CYAN)
            screen.blit(s_text, (10, 70))
        if lives > 1:
            l_text = small_font.render("EXTRA LIFE", True, GREEN)
            screen.blit(l_text, (10, 90))

        pygame.display.update()
        clock.tick(FPS)
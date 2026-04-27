import pygame
import random
import json
from config import *
from db import get_personal_best

def load_settings():
    default_settings = {"snake_color": [0, 255, 0], "grid": False, "sound": False}
    try:
        with open("settings.json", "r") as f:
            data = json.load(f)
            # Ensure the key exists in the loaded data
            if "snake_color" not in data:
                return default_settings
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return default_settings

def generate_food(snake_body, obstacles):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        pos = [x, y]
        if pos not in snake_body and pos not in obstacles:
            if random.random() < 0.15:
                return {'pos': pos, 'type': 'poison', 'color': DARK_RED, 'lifespan': 0}
            else:
                weight = random.choice([1, 2, 3])
                if weight == 1:
                    color = RED
                    lifespan = 0
                elif weight == 2:
                    color = YELLOW
                    lifespan = 8000
                else:
                    color = PURPLE
                    lifespan = 5000
                return {'pos': pos, 'type': 'normal', 'weight': weight, 'color': color, 'spawn_time': pygame.time.get_ticks(), 'lifespan': lifespan}

def generate_powerup(snake_body, obstacles, current_food):
    x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
    pos = [x, y]
    if pos not in snake_body and pos not in obstacles and pos != current_food['pos']:
        ptype = random.choice(['speed', 'slow', 'shield'])
        color = ORANGE if ptype == 'speed' else CYAN if ptype == 'slow' else BLUE
        return {'pos': pos, 'type': ptype, 'color': color, 'spawn_time': pygame.time.get_ticks(), 'lifespan': 8000}
    return None

def generate_obstacles(level, snake_pos):
    obstacles = []
    if level >= 3:
        num_blocks = level * 2
        while len(obstacles) < num_blocks:
            x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
            if abs(x - snake_pos[0]) > BLOCK_SIZE * 3 or abs(y - snake_pos[1]) > BLOCK_SIZE * 3:
                if [x, y] not in obstacles:
                    obstacles.append([x, y])
    return obstacles

def run_game(screen, font, username):
    settings = load_settings()
    sound_on = settings['sound']

    eat_sound = None
    if sound_on:
        try:
            eat_sound = pygame.mixer.Sound("C:/Users/Roar/Documents/GitHub/PP2/TSIS4/assets/eat.mp3")
        except:
            print("Sound files not found in assets/")
    snake_color = tuple(settings['snake_color'])
    grid_on = settings['grid']
    
    clock = pygame.time.Clock()
    snake_pos = [100, 60]
    snake_body = [[100, 60], [80, 60], [60, 60]]
    direction = 'RIGHT'
    change_to = direction
    score = 0
    level = 1
    base_speed = 10
    foods_eaten = 0
    pb = get_personal_best(username)

    obstacles = []
    current_food = generate_food(snake_body, obstacles)
    active_powerup = None
    powerup_effect = None
    powerup_end_time = 0
    shield_active = False

    running = True
    while running:
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None, None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP: change_to = 'UP'
                if event.key == pygame.K_DOWN: change_to = 'DOWN'
                if event.key == pygame.K_LEFT: change_to = 'LEFT'
                if event.key == pygame.K_RIGHT: change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN': direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP': direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT': direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT': direction = 'RIGHT'

        if direction == 'UP': snake_pos[1] -= BLOCK_SIZE
        if direction == 'DOWN': snake_pos[1] += BLOCK_SIZE
        if direction == 'LEFT': snake_pos[0] -= BLOCK_SIZE
        if direction == 'RIGHT': snake_pos[0] += BLOCK_SIZE

        collision = False
        if snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT:
            collision = True
        for block in snake_body:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                collision = True
        for obs in obstacles:
            if snake_pos[0] == obs[0] and snake_pos[1] == obs[1]:
                collision = True

        if collision:
            if shield_active:
                shield_active = False
                collision = False
                if snake_pos[0] < 0: snake_pos[0] = SCREEN_WIDTH - BLOCK_SIZE
                elif snake_pos[0] >= SCREEN_WIDTH: snake_pos[0] = 0
                elif snake_pos[1] < 0: snake_pos[1] = SCREEN_HEIGHT - BLOCK_SIZE
                elif snake_pos[1] >= SCREEN_HEIGHT: snake_pos[1] = 0
            else:
                return score, level

        snake_body.insert(0, list(snake_pos))
        ate_food = False

        if snake_pos == current_food['pos']:
            ate_food = True
            if current_food['type'] == 'poison':
                for _ in range(3):
                    if snake_body: snake_body.pop()
                if len(snake_body) <= 1:
                    return score, level
            else:
                score += 10 * current_food['weight']
                foods_eaten += 1
                if foods_eaten % 3 == 0:
                    level += 1
                    base_speed += 2
                    obstacles = generate_obstacles(level, snake_pos)
        else:
            snake_body.pop()

        if ate_food or (current_food['lifespan'] > 0 and current_time - current_food['spawn_time'] > current_food['lifespan']):
            current_food = generate_food(snake_body, obstacles)

        if active_powerup:
            if snake_pos == active_powerup['pos']:
                if active_powerup['type'] == 'speed':
                    powerup_effect = 'speed'
                    powerup_end_time = current_time + 5000
                elif active_powerup['type'] == 'slow':
                    powerup_effect = 'slow'
                    powerup_end_time = current_time + 5000
                elif active_powerup['type'] == 'shield':
                    shield_active = True
                active_powerup = None
            elif current_time - active_powerup['spawn_time'] > active_powerup['lifespan']:
                active_powerup = None
        else:
            if random.random() < 0.02:
                active_powerup = generate_powerup(snake_body, obstacles, current_food)

        if powerup_effect and current_time > powerup_end_time:
            powerup_effect = None

        current_speed = base_speed
        if powerup_effect == 'speed': current_speed += 5
        elif powerup_effect == 'slow': current_speed = max(5, current_speed - 5)

        screen.fill(BLACK)
        
        if grid_on:
            for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
                pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
            for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
                pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))

        for obs in obstacles:
            pygame.draw.rect(screen, WHITE, pygame.Rect(obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE))

        for i, pos in enumerate(snake_body):
            color = snake_color if not shield_active else BLUE
            pygame.draw.rect(screen, color, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(screen, current_food['color'], pygame.Rect(current_food['pos'][0], current_food['pos'][1], BLOCK_SIZE, BLOCK_SIZE))
        
        if active_powerup:
            pygame.draw.rect(screen, active_powerup['color'], pygame.Rect(active_powerup['pos'][0], active_powerup['pos'][1], BLOCK_SIZE, BLOCK_SIZE))

        score_txt = font.render(f"Score: {score} | Lvl: {level} | PB: {pb}", True, WHITE)
        screen.blit(score_txt, (10, 10))
        
        if powerup_effect:
            eff_txt = font.render(f"{powerup_effect.upper()}", True, ORANGE if powerup_effect=='speed' else CYAN)
            screen.blit(eff_txt, (10, 35))
        if shield_active:
            sh_txt = font.render("SHIELD", True, BLUE)
            screen.blit(sh_txt, (10, 60))

        pygame.display.update()
        clock.tick(current_speed)
import pygame
import random
import sys
import time

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (50, 153, 213)

font = pygame.font.SysFont("Verdana", 20)
game_over_font = pygame.font.SysFont("Verdana", 40)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Level-Up Snake")
clock = pygame.time.Clock()

def generate_food(snake_body):
    while True:
        x = random.randrange(0, SCREEN_WIDTH, BLOCK_SIZE)
        y = random.randrange(0, SCREEN_HEIGHT, BLOCK_SIZE)
        food_pos = [x, y]
        
        if food_pos not in snake_body:
            return food_pos

def game_over():
    screen.fill(BLACK)
    msg = game_over_font.render("GAME OVER", True, RED)
    screen.blit(msg, (SCREEN_WIDTH//2 - msg.get_width()//2, SCREEN_HEIGHT//2 - msg.get_height()//2))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    sys.exit()

snake_pos = [100, 60] # Head of the snake
snake_body = [[100, 60], [80, 60], [60, 60]] 

direction = 'RIGHT'
change_to = direction

score = 0
level = 1
speed = 10
foods_eaten = 0 

food_pos = generate_food(snake_body)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_pos[1] -= BLOCK_SIZE
    if direction == 'DOWN':
        snake_pos[1] += BLOCK_SIZE
    if direction == 'LEFT':
        snake_pos[0] -= BLOCK_SIZE
    if direction == 'RIGHT':
        snake_pos[0] += BLOCK_SIZE

    snake_body.insert(0, list(snake_pos))

    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 10
        foods_eaten += 1

        if foods_eaten % 3 == 0:
            level += 1
            speed += 2

        food_pos = generate_food(snake_body) 
    else:

        snake_body.pop()

    if (snake_pos[0] < 0 or snake_pos[0] >= SCREEN_WIDTH or 
        snake_pos[1] < 0 or snake_pos[1] >= SCREEN_HEIGHT):
        game_over()

    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    screen.fill(BLACK)

    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], BLOCK_SIZE, BLOCK_SIZE))

    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, BLUE)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 35))

    pygame.display.update()

    clock.tick(speed)
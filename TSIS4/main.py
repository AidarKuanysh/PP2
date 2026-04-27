import pygame
import sys
import json
from config import *
from db import init_db, save_result, get_top_10
from game import run_game

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Level-Up Snake")
font = pygame.font.SysFont("Verdana", 20)
title_font = pygame.font.SysFont("Verdana", 40)

init_db()

def draw_button(text, y, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rect = pygame.Rect(SCREEN_WIDTH//2 - 120, y, 240, 40)
    pygame.draw.rect(screen, GRAY if rect.collidepoint(mouse) else WHITE, rect)
    txt = font.render(text, True, BLACK)
    screen.blit(txt, (rect.x + 120 - txt.get_width()//2, rect.y + 10))
    
    if click[0] == 1 and action and rect.collidepoint(mouse):
        pygame.time.delay(200)
        return action
    return None

def main_menu(saved_username=""):
    username = saved_username
    input_active = True
    while True:
        screen.fill(BLACK)
        title = title_font.render("SNAKE GAME", True, GREEN)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 30))
        
        cursor = "_" if pygame.time.get_ticks() % 1000 < 500 else ""
        prompt = font.render(f"Username: {username}{cursor}", True, WHITE)
        screen.blit(prompt, (SCREEN_WIDTH//2 - prompt.get_width()//2, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    if len(username) < 15 and event.unicode.isalnum():
                        username += event.unicode

        if username:
            if draw_button("Play", 160, "play"): return username, "play"
            if draw_button("Leaderboard", 220, "leaderboard"): return username, "leaderboard"
            if draw_button("Settings", 280, "settings"): return username, "settings"
        
        if draw_button("Quit", 340, "quit"): 
            pygame.quit()
            sys.exit()

        pygame.display.update()

def leaderboard_screen():
    while True:
        screen.fill(BLACK)
        title = title_font.render("LEADERBOARD", True, YELLOW)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 20))
        
        top_10 = get_top_10()
        if top_10:
            y = 80
            for i, row in enumerate(top_10):
                txt = font.render(f"{i+1}. {row[0][:10]} | Score: {row[1]} | Lvl: {row[2]}", True, WHITE)
                screen.blit(txt, (50, y))
                y += 25
        else:
            err = font.render("No scores available.", True, RED)
            screen.blit(err, (SCREEN_WIDTH//2 - err.get_width()//2, 150))

        if draw_button("Back", 340, "back"): return
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def settings_screen():
    try:
        with open("settings.json", "r") as f:
            sett = json.load(f)
            if "snake_color" not in sett: sett["snake_color"] = list(GREEN)
            if "grid" not in sett: sett["grid"] = False
            if "sound" not in sett: sett["sound"] = False
    except:
        sett = {"snake_color": list(GREEN), "grid": False, "sound": False}
    
    colors = [list(GREEN), list(BLUE), list(PURPLE)]
    color_names = ["Green", "Blue", "Purple"]
    c_idx = colors.index(sett["snake_color"]) if sett["snake_color"] in colors else 0

    while True:
        screen.fill(BLACK)
        title = title_font.render("SETTINGS", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 30))

        grid_txt = "Grid: ON" if sett["grid"] else "Grid: OFF"
        if draw_button(grid_txt, 120, "grid"): sett["grid"] = not sett["grid"]
        
        snd_txt = "Sound: ON" if sett["sound"] else "Sound: OFF"
        if draw_button(snd_txt, 180, "sound"): sett["sound"] = not sett["sound"]

        col_txt = f"Color: {color_names[c_idx]}"
        if draw_button(col_txt, 240, "color"): 
            c_idx = (c_idx + 1) % len(colors)
            sett["snake_color"] = colors[c_idx]

        if draw_button("Save & Back", 320, "back"):
            with open("settings.json", "w") as f:
                json.dump(sett, f)
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

def game_over_screen(username, score, level):
    save_result(username, score, level)

    while True:
        screen.fill(BLACK)
        title = title_font.render("GAME OVER", True, RED)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 60))
        
        s_txt = font.render(f"Score: {score}   Level: {level}", True, WHITE)
        screen.blit(s_txt, (SCREEN_WIDTH//2 - s_txt.get_width()//2, 130))

        if draw_button("Retry", 210, "retry"): return "retry"
        if draw_button("Main Menu", 270, "menu"): return "menu"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

if __name__ == "__main__":
    current_username = ""
    
    while True:
        username, action = main_menu(current_username)
        current_username = username 
        
        while action == "play" or action == "retry":
            score, level = run_game(screen, font, current_username)
            if score is None: 
                pygame.quit()
                sys.exit()
            action = game_over_screen(current_username, score, level)
            
        if action == "leaderboard":
            leaderboard_screen()
        elif action == "settings":
            settings_screen()
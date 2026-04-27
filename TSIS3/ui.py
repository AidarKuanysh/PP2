import pygame
import sys
from persistence import load_leaderboard, save_settings

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 100, 255)

def draw_text(surface, text, font, color, rect, center=True):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    if center:
        text_rect.center = rect.center
    else:
        text_rect.topleft = rect.topleft
    surface.blit(text_obj, text_rect)

def draw_button(surface, rect, color, text, font):
    pygame.draw.rect(surface, color, rect)
    pygame.draw.rect(surface, BLACK, rect, 2)
    draw_text(surface, text, font, BLACK, rect)

def main_menu(screen, font):
    click = False
    while True:
        screen.fill(WHITE)
        draw_text(screen, "RACER: TSIS 3", font, BLACK, pygame.Rect(0, 50, 400, 100))

        mx, my = pygame.mouse.get_pos()

        btn_play = pygame.Rect(100, 200, 200, 50)
        btn_lb = pygame.Rect(100, 280, 200, 50)
        btn_set = pygame.Rect(100, 360, 200, 50)
        btn_quit = pygame.Rect(100, 440, 200, 50)

        buttons = {
            "PLAY": btn_play,
            "LEADERBOARD": btn_lb,
            "SETTINGS": btn_set,
            "QUIT": btn_quit
        }

        action = None
        for name, rect in buttons.items():
            color = GRAY if rect.collidepoint((mx, my)) else BLUE
            draw_button(screen, rect, color, name, font)
            if rect.collidepoint((mx, my)) and click:
                action = name

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if action:
            return action

        pygame.display.update()

def settings_menu(screen, font, settings):
    click = False
    difficulties = ["Easy", "Normal", "Hard"]
    colors = ["Blue", "Red", "Green"]
    
    while True:
        screen.fill(WHITE)
        draw_text(screen, "SETTINGS", font, BLACK, pygame.Rect(0, 50, 400, 50))

        mx, my = pygame.mouse.get_pos()

        btn_sound = pygame.Rect(50, 150, 300, 50)
        btn_diff = pygame.Rect(50, 230, 300, 50)
        btn_color = pygame.Rect(50, 310, 300, 50)
        btn_back = pygame.Rect(100, 450, 200, 50)

        draw_button(screen, btn_sound, GRAY, f"Sound: {'ON' if settings['sound'] else 'OFF'}", font)
        draw_button(screen, btn_diff, GRAY, f"Diff: {settings['difficulty']}", font)
        draw_button(screen, btn_color, GRAY, f"Color: {settings['car_color']}", font)
        draw_button(screen, btn_back, BLUE if btn_back.collidepoint((mx, my)) else GRAY, "BACK", font)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if click:
            if btn_sound.collidepoint((mx, my)):
                settings['sound'] = not settings['sound']
            elif btn_diff.collidepoint((mx, my)):
                idx = (difficulties.index(settings['difficulty']) + 1) % 3
                settings['difficulty'] = difficulties[idx]
            elif btn_color.collidepoint((mx, my)):
                idx = (colors.index(settings['car_color']) + 1) % 3
                settings['car_color'] = colors[idx]
            elif btn_back.collidepoint((mx, my)):
                save_settings(settings)
                return

        pygame.display.update()

def leaderboard_menu(screen, font, small_font):
    board = load_leaderboard()
    click = False
    while True:
        screen.fill(WHITE)
        draw_text(screen, "TOP 10", font, BLACK, pygame.Rect(0, 30, 400, 50))

        y_offset = 100
        for i, entry in enumerate(board):
            text = f"{i+1}. {entry['name']} - Score: {entry['score']} - Dist: {entry['distance']}m"
            draw_text(screen, text, small_font, BLACK, pygame.Rect(50, y_offset, 300, 30), center=False)
            y_offset += 30

        mx, my = pygame.mouse.get_pos()
        btn_back = pygame.Rect(100, 500, 200, 50)
        draw_button(screen, btn_back, BLUE if btn_back.collidepoint((mx, my)) else GRAY, "BACK", font)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                click = True

        if click and btn_back.collidepoint((mx, my)):
            return

        pygame.display.update()

def get_username(screen, font):
    name = ""
    active = True
    while active:
        screen.fill(WHITE)
        draw_text(screen, "Enter Name:", font, BLACK, pygame.Rect(0, 150, 400, 50))
        draw_text(screen, name + "_", font, BLUE, pygame.Rect(0, 250, 400, 50))
        draw_text(screen, "Press ENTER to start", pygame.font.SysFont(None, 24), BLACK, pygame.Rect(0, 350, 400, 50))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if name.strip() == "":
                        name = "Player"
                    return name
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    if len(name) < 10:
                        name += event.unicode
        pygame.display.update()
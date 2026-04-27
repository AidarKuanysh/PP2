import pygame
import sys
from persistence import load_settings, save_score
import ui
import racer

def main():
    pygame.init()
    
    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Racer - TSIS 3")
    
    font = pygame.font.SysFont("Verdana", 40)
    small_font = pygame.font.SysFont("Verdana", 20)
    
    settings = load_settings()
    username = None

    state = "MENU"

    while True:
        if state == "MENU":
            action = ui.main_menu(screen, font)
            if action == "PLAY":
                if not username:
                    state = "GET_NAME"
                else:
                    state = "GAME"
            elif action == "LEADERBOARD":
                state = "LEADERBOARD"
            elif action == "SETTINGS":
                state = "SETTINGS"
            elif action == "QUIT":
                pygame.quit()
                sys.exit()

        elif state == "GET_NAME":
            username = ui.get_username(screen, font)
            state = "GAME"

        elif state == "SETTINGS":
            ui.settings_menu(screen, font, settings)
            state = "MENU"

        elif state == "LEADERBOARD":
            ui.leaderboard_menu(screen, font, small_font)
            state = "MENU"

        elif state == "GAME":
            score, distance, finished = racer.run_game(screen, font, small_font, username, settings)
            
            if finished:
                # Calculate final score combination
                final_score = score + int(distance * 2) 
                save_score(username, final_score, distance)
            
            state = "MENU" # Return to main menu after death or quit

if __name__ == "__main__":
    main()
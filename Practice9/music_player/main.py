import pygame
import sys
from player import MusicPlayer

pygame.init()

screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Music Player")

player = MusicPlayer()
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next()
            elif event.key == pygame.K_b:
                player.prev()

    screen.fill((30, 30, 30))

    text = font.render(f"Track: {player.current_track()}", True, (255,255,255))
    screen.blit(text, (20, 100))

    pygame.display.flip()
    clock.tick(60)
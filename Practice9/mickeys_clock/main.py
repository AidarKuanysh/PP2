import pygame
import sys
from clock import MickeyClock


def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Mickey Clock")

    clock = pygame.time.Clock()
    app = MickeyClock(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        app.update()
        app.draw()

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
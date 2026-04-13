import pygame
import time


class MickeyClock:
    def __init__(self, screen):
        self.screen = screen

        # ✅ correct size handling
        self.width, self.height = self.screen.get_size()
        self.center = (self.width // 2, self.height // 2)

        # colors
        self.bg = (30, 30, 30)
        self.white = (255, 255, 255)

        # try loading image
        try:
            self.hand = pygame.image.load("C:/Users/Roar/Documents/GitHub/PP2/Practice9/mickeys_clock/images/mickey_hand.png").convert_alpha()
        except:
            # fallback if image missing
            self.hand = pygame.Surface((200, 20), pygame.SRCALPHA)
            pygame.draw.rect(self.hand, (255, 200, 150), (0, 0, 200, 20))

    def update(self):
        t = time.localtime()
        self.minutes = t.tm_min
        self.seconds = t.tm_sec

    def draw_hand(self, angle, scale=1.0):
        hand = pygame.transform.scale(
            self.hand,
            (
                int(self.hand.get_width() * scale),
                int(self.hand.get_height() * scale),
            ),
        )

        rotated = pygame.transform.rotate(hand, -angle)
        rect = rotated.get_rect(center=self.center)

        self.screen.blit(rotated, rect)

    def draw(self):
        self.screen.fill(self.bg)

        # draw clock circle
        pygame.draw.circle(self.screen, self.white, self.center, 200, 3)

        # calculate angles
        minute_angle = (self.minutes + self.seconds / 60) * 6
        second_angle = self.seconds * 6

        # ✅ Right hand = minutes
        self.draw_hand(minute_angle, 1.0)

        # ✅ Left hand = seconds
        self.draw_hand(second_angle, 0.7)

        # center dot
        pygame.draw.circle(self.screen, self.white, self.center, 5)
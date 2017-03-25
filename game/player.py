import pygame
from constants import SIZE


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pos = [0, 0]
        self.dir = [0, 0]

    def draw(self, screen):
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        pygame.draw.rect(
            screen,
            (255, 255, 255),
            (pixel_pos, (SIZE, SIZE))
        )

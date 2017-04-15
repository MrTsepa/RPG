import pygame
from constants import SIZE


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, health, damage, image, images, start_frame):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = image
        self.health = health
        self.dir = [0, 0]
        self.kicking = False
        self.damage = damage
        self.images = images
        self.start_frame = start_frame
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        self.rect = pygame.Rect(pixel_pos, [SIZE, SIZE])

    def draw(self, screen):
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        screen.blit(self.image, pixel_pos)


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, damage, image):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.damage = damage
        self.image = image
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        self.rect = pygame.Rect(pixel_pos, [SIZE, SIZE])

    def draw(self, screen):
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        screen.blit(self.image, pixel_pos)

import pygame
from constants import SIZE


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, health, image, images, start_frame):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.image = image
        self.health = health
        self.vel = [0, 0]
        self.direction = [0, 1]
        self.items = []
        self.images = images
        self.start_frame = start_frame
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        self.rect = pygame.Rect(pixel_pos, [SIZE, SIZE])

    def get_damage(self):
        return 2 + sum([item.damage for item in self.items])

    def draw(self, screen):
        pixel_pos = (
            self.pos[0] * SIZE,
            self.pos[1] * SIZE
        )
        if self.direction == [0, -1]:
            self.image = self.images[9]
        if self.direction == [0, 1]:
            self.image = self.images[0]
        if self.direction == [-1, 0]:
            self.image = self.images[3]
        if self.direction == [1, 0]:
            self.image = self.images[6]
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

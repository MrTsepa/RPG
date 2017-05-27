import pygame
from enum import Enum
from data.constants import SIZE


class Ability(Enum):
    Fire = 1
    Ice = 2
    Heal = 3


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, health, image, images, start_frame, abilities, mana, stats):
        pygame.sprite.Sprite.__init__(self)
        self.tpos = pos
        self.image = image
        self.health = health
        self.vel = [0, 0]
        self.direction = [1, 0]
        self.h_items = []  # h - hand
        self.images = images
        self.abilities = abilities
        self.start_frame = start_frame
        self.mana = mana
        self.stats = stats
        self.regen_time = 0
        self.debuff = 'None'
        self.pos = [self.tpos[0] * SIZE, self.tpos[1] * SIZE]
        self.rect = pygame.Rect(self.pos, [SIZE, SIZE])

    def get_damage(self):
        return 2 + sum([item.damage for item in self.h_items])

    def draw(self, screen):

        if self.direction == [0, -1]:
            self.image = self.images[9]
        if self.direction == [0, 1]:
            self.image = self.images[0]
        if self.direction == [-1, 0]:
            self.image = self.images[3]
        if self.direction == [1, 0]:
            self.image = self.images[6]
        screen.blit(self.image, self.pos)


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, image):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
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


class Scrolls(Item):
    def __init__(self, pos, image):
        Item.__init__(self, pos, image)


class Weapon(Item):
    def __init__(self, pos, damage, image):
        Item.__init__(self, pos, image)
        self.damage = damage


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, image, damage, direction, speciffic, vel=1):
        pygame.sprite.Sprite.__init__(self)
        self.pos = list(player.pos)
        self.damage = damage
        self.image = image
        self.vel = vel
        self.direction = direction
        self.shooter = player
        self.speciffic = speciffic
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
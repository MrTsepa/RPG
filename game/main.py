#-*-coding: utf8-*-
import pygame
from load_images import *
from engine import Engine
from player import *
from Camera import *

pygame.init()
size = [2800, 1000]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert_alpha()

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

engine = Engine()
hero = Player([1, 1], 1000, 10)
enemy = Player([4, 4], 100, 1)
sworld = Item([9, 11], 10, sworld_im)
camera = Camera(hero.pos, size)
engine.players.add(hero, enemy)
engine.items.add(sworld)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                hero.kicking = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        hero.dir = [-1, 0]
    if keys[pygame.K_d]:
        hero.dir = [1, 0]
    if keys[pygame.K_w]:
        hero.dir = [0, -1]
    if keys[pygame.K_s]:
        hero.dir = [0, 1]
    engine.update_players()
    screen.fill((0, 100, 0))
    engine.draw(screen)

    if pygame.sprite.collide_rect(hero, sworld):
        hero.damage += sworld.damage
        sworld.kill()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

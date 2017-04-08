#-*-coding: utf8-*-
import pygame
from load_images import *
from engine import Engine
from player import *
from Camera import *
from game.animat import param


pygame.init()
size = [5500, 1000]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

engine = Engine()
hero = Player([1, 1], 1000, 10, 'ss_arr[0]')
enemy = Player([4, 4], 100, 1, 'empety')
vasa = Player([19, 19], 100, 1, 'empety')
anton = Player([23, 11], 100, 1, 'empety')
sworld = Item([35, 37], 10, sworld_im)
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


    class xparam(param):
        def __init__(self, sprite):
            self.sprite = sprite
        def get(self):
            return self.sprite.pos[0]

        def set(self, value):
            self.sprite.pos[0] = value

    if pygame.sprite.collide_rect(hero, sworld):
        hero.damage += sworld.damage
        sworld.kill()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

#-*-coding: utf8-*-
import pygame
from load_images import *
from engine import Engine
from player import *

pygame.init()
size = [600, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

engine = Engine()
hero = Player([1, 1], 100, 1, 'empety')
enemy = Player([9, 9], 100, 1, 'empety')
sworld = Item([9, 11], 10, sworld_im)
engine.players.add(hero, enemy)
engine.items.add(sworld)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                hero.dir = [0, 1]
            if event.key == pygame.K_w:
                hero.dir = [0, -1]
            if event.key == pygame.K_a:
                hero.dir = [-1, 0]
            if event.key == pygame.K_d:
                hero.dir = [1, 0]
            if event.key == pygame.K_SPACE:
                hero.kicking = True
    engine.update_players()
    screen.fill((0, 100, 0))
    engine.draw(screen)
    if pygame.sprite.collide_rect(hero, sworld):
        hero.damage += sworld.damage
        sworld.kill()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()

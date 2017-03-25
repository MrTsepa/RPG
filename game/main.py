#-*-coding: utf8-*-
import pygame
from engine import Engine
from player import Player

pygame.init()
size = [600, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

engine = Engine()
hero = Player()
engine.players.add(hero)

hero.pos = [2, 2]
hero.dir = [0, 0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                hero.dir = [0, 1]

    engine.update_players()

    screen.fill((0, 100, 0))
    engine.draw(screen)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

#-*-coding: utf8-*-
import pygame
from engine import Engine

pygame.init()
size = [600, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
engine = Engine()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 100, 0))
    engine.draw(screen)

    pygame.display.flip()
    clock.tick(30)
pygame.quit()

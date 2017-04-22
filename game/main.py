#-*-coding: utf8-*-

import pygame
from load_images import *
from engine import Engine
from player import *
from Camera import *
from spritesheet import *
from Bar import *
pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = pygame.font.Font(None, 20)

engine = Engine()

ss = spritesheet(ss_image)
ss_arr = make_spritesheet_array(ss)

hero = Player([1, 1], 700, ss_arr[0], ss_arr, 0)
enemy = Player([4, 4], 100, ss_arr[0], ss_arr, 0)
sworld = Item([9, 11], 10, sworld_im)
hp_bar = Bar(20, [50, 10], 1)
camera = Camera(hero.pos, size)
engine.players.add(hero, enemy)
engine.items.add(sworld)

world_image = pygame.Surface((5500, 1000))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                engine.make_kick(hero)
            if event.key == pygame.K_e:
                engine.take_item(hero)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        hero.vel = [-1, 0]
        hero.direction = [-1, 0]
    if keys[pygame.K_d]:
        hero.vel = [1, 0]
        hero.direction = [1, 0]
    if keys[pygame.K_w]:
        hero.vel = [0, -1]
        hero.direction = [0, -1]
    if keys[pygame.K_s]:
        hero.vel = [0, 1]
        hero.direction = [0, 1]
    hp_bar.set_bar(hero.health)
    engine.update_players()

    screen.fill((0, 100, 0))
    engine.draw(world_image)
    screen.blit(
        world_image, (
            min(-hero.pos[0] * SIZE + 400, 0),
            min(-hero.pos[1] * SIZE + 300, 0)
        )
    )

    screen.blit(
        font.render(
            'Damage: ' + str(hero.get_damage()),
            True,
            [255, 255, 255]
        ),
        (700, 500)
    )


    hp_bar.draw_x_bar([0, 100, 0], screen)
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

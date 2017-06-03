#-*-coding: utf-8*-

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)

from data.Bar import *
from data.Camera import *
from data.player import *
from data.spritesheet import *
from engine import Engine
from load_images import *
from data.AI import *
from data.Fractions import *


pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

engine = Engine()
ai = PathFinder()

ss = spritesheet(os.path.join(IMAGES_DIR, 'Hero.png'))
ss_arr = make_spritesheet_array(ss)

hero = Player([1, 1], 700, ss_arr[0], ss_arr, 0, [Ability.Fire], 100, [10, 10])
enemy = Player([10, 11], 20, ss_arr[0], ss_arr, 0, [], 0, [0, 0])
enemy1 = Player([113, 8], 100, ss_arr[0], ss_arr, 0, [], 0, [0, 0])
sworld = Weapon([9, 11], 10, sworld_im)
Heal_scroll = Scrolls([9, 0], sworld_im)  # TODO: Make image of Heal_scroll
hp_bar = ClewerBar(10, [130, 545], 166, hero.health)
mana_bar = ClewerBar(9, [130, 560], 159, hero.mana)
camera = Camera(hero.pos, size)
enemies.add(enemy, enemy1)

engine.players.add(hero, enemies)
engine.items.add(sworld)

world_image = pygame.Surface((7500, 3000))
inv_image = pygame.Surface((288, 32))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                engine.take_item(hero)
            if event.key == pygame.K_SPACE:
                engine.make_kick(hero)
            if event.key == pygame.K_UP:
                hero.direction = [0, -1]
            if event.key == pygame.K_DOWN:
                hero.direction = [0, 1]
            if event.key == pygame.K_RIGHT:
                hero.direction = [1, 0]
            if event.key == pygame.K_LEFT:
                hero.direction = [-1, 0]
            if event.key == pygame.K_1:
                if hero.mana - 10 >= 0:
                    engine.use_ability(hero, Ability.Fire)
                    hero.mana -= 10
            if event.key == pygame.K_2:
                if hero.mana - 12 >= 0:
                    engine.use_ability(hero, Ability.Ice)
                    hero.mana -= 12
            if event.key == pygame.K_3:
                if hero.mana - 50 >= 0:
                    engine.use_ability(hero, Ability.Heal)
                    hero.mana -= 50
            if event.key == pygame.K_5:
                engine.inv_add_item
    for punchenemy in enemies:
        engine.make_kick(punchenemy)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        hero.vel = [-4, 0]
        hero.direction = [-10, 0]
        # engine.update_players()
    if keys[pygame.K_d]:
        hero.vel = [4, 0]
        hero.direction = [10, 0]
        # engine.update_players()
    if keys[pygame.K_w]:
        hero.vel = [0, -4]
        hero.direction = [0, -10]
        # engine.update_players()
    if keys[pygame.K_s]:
        hero.vel = [0, 4]
        hero.direction = [0, 10]
        # engine.update_players()
    hp_bar.update_bar(hero.health)
    mana_bar.update_bar(hero.mana)
    engine.update_players()
    screen.fill((0, 100, 0))
    hero.regen_time += 1
    if hero.regen_time >= 60:
        if hero.mana + hero.stats[1] <= mana_bar.true_vaule:
            hero.mana += hero.stats[1]
        if hero.health + hero.stats[0] <= hp_bar.true_vaule:
            hero.health += hero.stats[0]
        hero.regen_time = 0
    inv = engine.make_screen_to_inv_screen([9, 1], inv_image, 32, slot_image)
    engine.draw(world_image)
    for movenemy in enemies:
        ai.path_to_player(hero, movenemy)
    if hero.health > 700:
        hero.health = 700
    screen.blit(
        world_image, (
            min(-hero.pos[0] + 400, 0),
            min(-hero.pos[1] + 300, 0)
        )
    )
    screen.blit(inv, [1, 1])
    engine.draw_inv_item(screen)
    screen.blit(hero_im, [10, 510])
    hp_bar.draw_X_Bar([0, 200, 0], screen)
    mana_bar.draw_X_Bar([0, 0, 200], screen)
    screen.blit(hero_hp_bar, [0, 500])
    if pygame.sprite.collide_rect(hero, sworld):
        hero.damage += sworld.damage
        sworld.kill()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

#-*-coding: utf8-*-
import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)

from data.Bar import *
from data.Camera import *
from data.player import *
from data.spritesheet import *
from engine import Engine
from load_images import *
from data.AI import *
from data.Paths import *

pygame.init()
size = [800, 600]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

engine = Engine()
ai = PathFinder()

ss = spritesheet(ss_image)
ss_arr = make_spritesheet_array(ss)

hero = Player([1, 1], 700, ss_arr[0], ss_arr, 0)
enemy = Player([4, 4], 100, ss_arr[0], ss_arr, 0)
enemy1 = Player([113, 8], 100, ss_arr[0], ss_arr, 0)
sworld = Item([9, 11], 10, sworld_im)
hp_bar = ClewerBar(10, [130, 545], 166, hero.health)
mana_bar = ClewerBar(9, [130, 560], 159, 100)
camera = Camera(hero.pos, size)
enemies = pygame.sprite.Group()
enemies.add(enemy, enemy1)

engine.players.add(hero, enemies)
engine.items.add(sworld)

world_image = pygame.Surface((5500, 1000))

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
    if enemy in engine.players:
        engine.make_kick(enemy)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        hero.vel = [-1, 0]
        hero.direction = [-1, 0]
        engine.update_players()
    if keys[pygame.K_d]:
        hero.vel = [1, 0]
        hero.direction = [1, 0]
        engine.update_players()
    if keys[pygame.K_w]:
        hero.vel = [0, -1]
        hero.direction = [0, -1]
        engine.update_players()
    if keys[pygame.K_s]:
        hero.vel = [0, 1]
        hero.direction = [0, 1]
        engine.update_players()
    hp_bar.update_bar(hero.health)
    mana_bar.update_bar(100)
    engine.update_players()
    screen.fill((0, 100, 0))
    engine.draw(world_image)
    ai.path_to_player(hero, enemy)
    screen.blit(
        world_image, (
            min(-hero.pos[0] * SIZE + 400, 0),
            min(-hero.pos[1] * SIZE + 300, 0)
        )
    )
    screen.blit(hero_im, [10, 510])
    hp_bar.draw_X_Bar([0, 200, 0], screen)
    mana_bar.draw_X_Bar([0, 0, 200], screen)
    screen.blit(hero_hp_bar, [0, 500])
    if pygame.sprite.collide_rect(hero, sworld):
        hero.damage += sworld.damage
        sworld.kill()
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

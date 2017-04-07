import pygame
from  load_images import *
from player import Player
from constants import SIZE
from constants import solids
from levels import level1


class Engine:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.map = level1
        self.items = pygame.sprite.Group()
    def update_players(self):
        for player in self.players:
            x1 = player.pos[0] + player.dir[0]
            y1 = player.pos[1] + player.dir[1]
            if self.map[y1][x1] not in solids:
                player.pos[0] += player.dir[0]
                player.pos[1] += player.dir[1]
            player.dir = [0, 0]
            if player.kicking:
                for en in self.players:
                    if abs(en.pos[0] - player.pos[0]) == 1:
                        if abs(en.pos[1] - player.pos[1]) == 0:
                            en.health -= player.damage
                            player.kicking = False
                    if abs(en.pos[0] - player.pos[0]) == 0:
                        if abs(en.pos[1] - player.pos[1]) == 1:
                            en.health -= player.damage
                            player.kicking = False
                    if en.health <= 0:
                        en.kill()

    def draw(self, screen):
        y = 0
        for line in self.map:
            x = 0
            for symb in line:
                if symb == '*':
                    screen.blit(tree_im, [x, y])
                if symb == '_':
                    screen.blit(grass_im, [x, y])
                if symb == '#':
                    screen.blit(mount_im, [x, y])
                if symb == '+':
                    screen.blit(water_im, [x, y])
                if symb == '=':
                    screen.blit(wood_im, [x, y])
                if symb == '-':
                    screen.blit(sand_im, [x, y])
                if symb == '^':
                    screen.blit(tree_desert_im, [x, y])

                x += SIZE
            y += SIZE
        for player in self.players:
            player.draw(screen)
        for item in self.items:
            item.draw(screen)

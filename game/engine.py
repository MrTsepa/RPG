import pygame
from player import Player
from constants import SIZE
from levels import level1


class Engine:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.map = level1

    def update_players(self):
        for player in self.players:
            x = player.pos[0] + player.dir[0]
            y = player.pos[1] + player.dir[1]
            if self.map[y][x] == '_':
                player.pos[0] += player.dir[0]
                player.pos[1] += player.dir[1]
            player.dir = [0, 0]

    def draw(self, screen):
        y = 0
        for line in self.map:
            x = 0
            for symb in line:
                if symb == '*':
                    pygame.draw.rect(
                        screen,
                        (0, 250, 0),
                        ((x, y), (SIZE, SIZE))
                    )
                x += SIZE
            y += SIZE
        for player in self.players:
            player.draw(screen)


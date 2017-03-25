import pygame
from player import Player


class Engine:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.map = [
            '***********',
            '*_________*',
            '*_________*',
            '*__*__*___*',
            '*_________*',
            '*_________*',
            '*_________*',
            '*_________*',
            '*_________*',
            '*_________*',
            '***********'
        ]

    def update_players(self):
        for player in self.players:
            x = player.pos[0] + player.dir[0]
            y = player.pos[1] + player.dir[1]
            if self.map[y][x] == '_':
                player.pos[0] += player.dir[0]
                player.pos[1] += player.dir[1]

    def draw(self, screen):
        y = 0
        for line in self.map:
            x = 0
            for symb in line:
                if symb == '*':
                    pygame.draw.rect(screen, (0,250, 0), ((x, y), (30, 30)))
                x += 30
            y += 30
        for player in self.players:
            pygame.draw.rect(screen, (0,250, 0), ((x*30, y*30), (30, 30)))


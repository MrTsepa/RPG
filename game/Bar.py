import pygame


class Bar:
    def __init__(self, height, pos, add):
        self.height = height
        self.value = 0
        self.pos = pos
        self.add = add

    def set_bar(self, value):
        self.value = value

    def draw_x_bar(self, color, screen):
        pygame.draw.rect(screen, (color), (self.pos[0], self.pos[1], self.value * self.add, self.height))

    def draw_y_bar(self, color, screen):
        pygame.draw.rect(screen, (color), (self.pos[0], self.pos[1], self.height, self.value * self.add))
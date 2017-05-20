import pygame

class Bar ():
    def __init__(self, height, pos, add):
        self.height = height
        self.value = 0
        self.pos = pos
        self.add = add

    def set_Bar(self, value):
        self.value = value

    def draw_X_Bar(self, color, screen):
        pygame.draw.rect(screen, (color), (self.pos[0], self.pos[1], self.value * self.add, self.height))

    def draw_Y_Bar(self, color, screen):
        pygame.draw.rect(screen, (color), (self.pos[0], self.pos[1], self.height, self.value * self.add))


class ClewerBar:
    def __init__(self, height, pos, true_lenght, value):
        self.height = height
        self.value = 0
        self.pos = pos
        self.add = true_lenght / value

    def update_bar(self, value):
        self.value = value
    def draw_X_Bar(self, color, screen):
        pygame.draw.rect(screen, (color), (self.pos[0], self.pos[1], self.value * self.add, self.height))

    def draw_Y_Bar(self, color, screen):
        pygame.draw.rect(screen, (color), (self.pos[0], self.pos[1], self.height, self.value * self.add))

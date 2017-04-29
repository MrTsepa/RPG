import pygame


class PathFinder:
    def __init__(self):
        pass

    def path_to_player(self, to_what, who):
        if to_what.pos[0] > who.pos[0]:
            who.vel[0] = 1
            if to_what.pos[1] > who.pos[1]:
                who.vel[1] = 1
                who.direction = [0, 1]
            if to_what.pos[1] < who.pos[1]:
                who.vel[1] = -1
                who.direction = [0, -1]
            if to_what.pos[1] == who.pos[1]:
                who.vel[1] = 0
                who.direction = [1, 0]
        if to_what.pos[0] < who.pos[0]:
            who.vel[0] = -1
            if to_what.pos[1] > who.pos[1]:
                who.vel[1] = 1
                who.direction = [0, 1]
            if to_what.pos[1] < who.pos[1]:
                who.vel[1] = -1
                who.direction = [0, -1]
            if to_what.pos[1] == who.pos[1]:
                who.vel[1] = 0
                who.direction = [-1, 0]
        if to_what.pos[0] == who.pos[0]:
            if to_what.pos[1] > who.pos[1]:
                who.vel[1] = 1
                who.direction = [0, 1]
            if to_what.pos[1] < who.pos[1]:
                who.vel[1] = -1
                who.direction = [0, 1]
            if to_what.pos[1] == who.pos[1]:
                who.vel[1] = 0
                who.direction = [1, 0]

    def path_to_point(self, points, who):
        for to_what in points:
            self.path_to_player(to_what, who)

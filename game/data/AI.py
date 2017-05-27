import pygame


class PathFinder:
    def __init__(self):
        pass
    def path_to_player(self, to_what, who):
        if who.pos[0] - to_what.pos[0] < 10 or to_what.pos[0] - who.pos[0] > -10:
            if who.pos[1] - to_what.pos[1] < 10 or to_what.pos[1] - who.pos[1] > -10:
                if who.debuff != 'iced':
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
            if to_what[0] > who.pos[0]:
                who.vel[0] = 1
                if to_what[1] > who.pos[1]:
                    who.vel[1] = 1
                    who.direction = [0, 1]
                if to_what[1] < who.pos[1]:
                    who.vel[1] = -1
                    who.direction = [0, -1]
                if to_what[1] == who.pos[1]:
                    who.vel[1] = 0
                    who.direction = [1, 0]
            if to_what[0] < who.pos[0]:
                who.vel[0] = -1
                if to_what[1] > who.pos[1]:
                    who.vel[1] = 1
                    who.direction = [0, 1]
                if to_what[1] < who.pos[1]:
                    who.vel[1] = -1
                    who.direction = [0, -1]
                if to_what[1] == who.pos[1]:
                    who.vel[1] = 0
                    who.direction = [-1, 0]
            if to_what[0] == who.pos[0]:
                if to_what[1] > who.pos[1]:
                    who.vel[1] = 1
                    who.direction = [0, 1]
                if to_what[1] < who.pos[1]:
                    who.vel[1] = -1
                    who.direction = [0, 1]
                if to_what[1] == who.pos[1]:
                    who.vel[1] = 0
                    who.direction = [1, 0]
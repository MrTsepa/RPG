import pygame


class spritesheet(object):
    def __init__(self, image):
        self.sheet = image

    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image


def make_spritesheet_array(sprsht):
    ss_arr = []
    for y in range(0, 80, 20):
        for x in range(0, 60, 20):
            image_expl = sprsht.image_at((x, y, 20, 20))
            ss_arr.append(image_expl)
    return ss_arr

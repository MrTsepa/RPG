class Camera:
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def centralize(self, pos_pl):
        self.pos[0] = pos_pl[0] - (self.size[0] / 2)
        self.pos[1] = pos_pl[1] - (self.size[1] / 2)

    def get_local_pos(self, g_pos):
        local_pos = [0, 0]
        local_pos[0] = g_pos[0] - self.pos[0]
        local_pos[1] = g_pos[1] - self.pos[1]
        return local_pos

    def draw(self, screen, sprite_pos, sprite_image):
        image_pos = [0, 0]
        new_image_pos = [0, 0]
        image_pos[0] = sprite_pos[0] - self.pos[0]
        image_pos[1] = sprite_pos[1] - self.pos[1]
        new_image_pos[0] = image_pos[0] - (sprite_image.get_width()/2)
        new_image_pos[1] = image_pos[1] - (sprite_image.get_height()/2)
        screen.blit(sprite_image, new_image_pos)
    a= 0
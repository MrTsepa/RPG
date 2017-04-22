import os
import pygame

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
print(IMAGES_DIR)

size = [2800, 1000]
screen = pygame.display.set_mode(size)

tree_im = pygame.image.load(os.path.join(IMAGES_DIR, 'sum_tree.png')).convert_alpha()
grass_im = pygame.image.load(os.path.join(IMAGES_DIR, 'Grass.png')).convert_alpha()
mount_im = pygame.image.load(os.path.join(IMAGES_DIR, 'mount.png')).convert_alpha()
sworld_im = pygame.image.load(os.path.join(IMAGES_DIR, 'Sworld.png')).convert_alpha()
wood_im = pygame.image.load(os.path.join(IMAGES_DIR, 'wood.png')).convert_alpha()
water_im = pygame.image.load(os.path.join(IMAGES_DIR, 'Water.png')).convert_alpha()
sand_im = pygame.image.load(os.path.join(IMAGES_DIR, 'sand.png')).convert_alpha()
tree_desert_im = pygame.image.load(os.path.join(IMAGES_DIR, 'des_tree.png')).convert_alpha()

ss_image = pygame.image.load(os.path.join(IMAGES_DIR, 'Hero.png')).convert_alpha()
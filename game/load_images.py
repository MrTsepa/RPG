import os
import pygame

IMAGES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
print(IMAGES_DIR)

size = [2800, 1000]
screen = pygame.display.set_mode(size)

tree_im = pygame.image.load(os.path.join(IMAGES_DIR, 'sum_tree.png'))
grass_im = pygame.image.load(os.path.join(IMAGES_DIR, 'Grass.png'))
mount_im = pygame.image.load(os.path.join(IMAGES_DIR, 'mount.png'))
sworld_im = pygame.image.load(os.path.join(IMAGES_DIR, 'Sworld.png'))
wood_im = pygame.image.load(os.path.join(IMAGES_DIR, 'wood.png'))
water_im = pygame.image.load(os.path.join(IMAGES_DIR, 'Water.png'))
sand_im = pygame.image.load(os.path.join(IMAGES_DIR, 'sand.png'))
tree_desert_im = pygame.image.load(os.path.join(IMAGES_DIR, 'des_tree.png'))

ss_image = pygame.image.load(os.path.join(IMAGES_DIR, 'Hero.png')).convert_alpha()
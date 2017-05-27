from data.constants import SIZE
from data.constants import solids
from data.levels import level1
from load_images import *
from data.player import *

class Engine:
    def __init__(self):
        self.players = pygame.sprite.Group()
        self.map = level1
        self.items = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
    def update_players(self):
        player_poses = [p.pos for p in self.players]
        item_poses = [p.pos for p in self.items]
        for player in self.players:
            x1 = player.pos[0] + player.vel[0]
            y1 = player.pos[1] + player.vel[1]
            if self.map[y1][x1] in solids:
                continue
            if [x1, y1] in player_poses:
                continue
            if [x1, y1] in item_poses:
                continue
            player.pos[0] += player.vel[0]
            player.pos[1] += player.vel[1]
            player.vel = [0, 0]
            #bullet_hit = pygame.sprite.spritecollideany(player, self.bullets)
            #if bullet_hit is not None:
            #    if player != bullet_hit.shooter:
            #        bullet_hit.kill()
            #        player.health -= bullet_hit.damage
            for bullet in self.bullets:
                if player != bullet.shooter:
                    if player.pos[0] == bullet.pos[0] and player.pos[1] == bullet.pos[1]:
                        bullet.kill()
                        player.health -= bullet.damage
        for bullet in self.bullets:
            bullet.pos[0] += bullet.vel * bullet.direction[0]
            bullet.pos[1] += bullet.vel * bullet.direction[1]

    def make_kick(self, player):
        print("Punch! kiking by player in " + str(player.pos) )
        for target in self.players:
            if (
                player.pos[0] + player.direction[0],
                player.pos[1] + player.direction[1]
            ) == (
                target.pos[0],
                target.pos[1]
            ):
                target.health -= player.get_damage()
            if target.health <= 0:
                target.kill()

    def shoot(self, bullet):
        self.bullets.add(bullet)

    def take_item(self, player):
        for item in self.items:
            if (
                player.pos[0] + player.direction[0],
                player.pos[1] + player.direction[1]
            ) == (
                item.pos[0],
                item.pos[1]
            ):
                player.h_items.append(item)
                item.kill()


    def use_ability(self, player, type):
        if type == Ability.Fire:
            bullet = Bullet(player, sworld_im, 10, player.direction)           # TODO: Fire image
            self.shoot(bullet)

    def draw(self, screen):
        y = 0
        for line in self.map:
            x = 0
            for symb in line:
                if symb == '*':
                    screen.blit(tree_im, [x, y])
                if symb == '_':
                    screen.blit(grass_im, [x, y])
                if symb == '#':
                    screen.blit(mount_im, [x, y])
                if symb == '+':
                    screen.blit(water_im, [x, y])
                if symb == '=':
                    screen.blit(wood_im, [x, y])
                if symb == '-':
                    screen.blit(sand_im, [x, y])
                if symb == '^':
                    screen.blit(tree_desert_im, [x, y])

                x += SIZE
            y += SIZE
        for player in self.players:
            player.draw(screen)
        for item in self.items:
            item.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)
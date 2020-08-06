import pygame
from spritesheet import SpriteSheet

class Shadow(object):
    def __init__(self, group):
        sprite = SpriteSheet('data/spritesheet.png')
        self.shadows = {'HeroRun': sprite.get_sprite(33, 32, 8, 3),
                        'HeroGun': sprite.get_sprite(82, 32, 10, 3)}
        self.group = group
    def create(self, name, pos_x, pos_y, width, height):
        shadow_fx = pygame.sprite.Sprite(self.group)
        shadow_fx.image = self.shadows[name]
        shadow_fx.rect = pygame.Rect(pos_x, pos_y, width, height)
        return shadow_fx

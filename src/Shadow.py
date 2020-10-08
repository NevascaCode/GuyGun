import pygame
from .MyTypes import Group, Sprite, Entity
from src.spritesheet import SpriteSheet

class Shadow(object):
    def __init__(self, group: Group):
        sprite = SpriteSheet('res/sprite/spritesheet.png')
        self.shadows: Sprite = {'HeroRun': sprite.get_sprite(33, 32, 8, 3),
                                'HeroGun': sprite.get_sprite(82, 32, 10, 3)}
        self.group = group

    def create(self, name: str, pos_x: int, pos_y: int, width: int, height: int)-> Entity:
        shadow: Entity = pygame.sprite.Sprite(self.group)
        shadow.image = self.shadows[name]
        shadow.rect = pygame.Rect(pos_x, pos_y, width, height)
        return shadow

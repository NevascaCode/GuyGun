import pygame
from src.MyTypes import Sprite, Group, Rect
from src.spritesheet import SpriteSheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int, *groups: Group):
        super().__init__(*groups)
        self.image: Sprite = SpriteSheet('res/sprite/spritesheet.png').get_sprite(16, 38, 9, 10)
        self.image: Sprite = pygame.transform.scale(self.image, (27, 30))
        self.rect: Rect = pygame.Rect(pos_x, pos_y, 9, 10)
    def update(self):
        ...

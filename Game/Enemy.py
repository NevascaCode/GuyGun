import pygame
from spritesheet import SpriteSheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x, pos_y, *groups):
        super().__init__(*groups)
        self.image = SpriteSheet('data/spritesheet.png').get_sprite(16, 38, 9, 10)
        self.image = pygame.transform.scale(self.image, (27, 30))
        self.rect = pygame.Rect(pos_x, pos_y, 9, 10)
    def update(self):
        ...

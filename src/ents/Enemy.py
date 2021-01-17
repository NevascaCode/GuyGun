import pygame
from src.spritesheet import SpriteSheet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int, *groups):
        super().__init__(*groups)
        self.lifes = 3
        self.image = SpriteSheet('res/sprite/spritesheet.png').get_sprite(16, 38, 9, 10)
        self.image = pygame.transform.scale(self.image, (27, 30))
        self.rect = pygame.Rect(pos_x, pos_y, 27, 30)
    def update(self):
        if self.lifes == 0:
            self.kill()

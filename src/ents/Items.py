import pygame
from src.spritesheet import SpriteSheet

class Gun(pygame.sprite.Sprite):
    def __init__(self, pos_x: int, pos_y: int, *groups):
        super().__init__(*groups)
        self.type: str = 'Gun'
        self.perma_item: str  = 'GunPerma'
        spritesheet= SpriteSheet('res/sprite/spritesheet.png')
        self.sprites = [spritesheet.get_sprite(0, 0, 11, 7),
                                spritesheet.get_sprite(12, 0, 11, 7),
                                spritesheet.get_sprite(24, 0, 11, 7),
                                spritesheet.get_sprite(36, 0, 11, 7)]
        self.sprite_count: int = 0
        self.image = spritesheet.get_sprite(0, 0, 11, 7)
        self.image = pygame.transform.scale(self.image, [22, 14])
        self.rect = pygame.Rect(pos_x, pos_y, 35, 28)

    def Pickup(self):
        return ['HeroGun', True]

    def update(self):
        if self.sprite_count >= len(self.sprites):
            self.sprite_count = 0

        self.image = self.sprites[int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, [44, 28])

        self.sprite_count += 0.075

import pygame
from .res.sprites.spritesheet import SpriteSheet

class Gun(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.perma_item = 'GunPerma'
        self.spritesheet = SpriteSheet('BlockSelector/Game/res/sprites/spritesheet.png')
        self.sprites = [self.spritesheet(0, 0, 11, 7),
                        self.spritesheet(12, 0, 11, 7),
                        self.spritesheet(24, 0, 11, 7),
                        self.spritesheet(36, 0, 11, 7)]
        self.sprite_count = 0
        self.image = self.spritesheet(0, 0, 11, 7)
        self.image = pygame.transform.scale(self.image, [44, 28])
        self.rect = pygame.Rect(300, 400, 35, 28)

    def Pickup(self):
        return ['HeroGun', True]

    def update(self):
        if self.sprite_count >= len(self.sprites):
            self.sprite_count = 0

        self.image = self.sprites[int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, [44, 28])

        self.sprite_count += 0.075

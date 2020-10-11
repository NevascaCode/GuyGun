import pygame
from src.MyTypes import Sprite, Group, FileSpriteSheet, Rect, Estate
from src.spritesheet import SpriteSheet

class Gun(pygame.sprite.Sprite):
    __slots__ = ('type', 'perma_item', 'sprites', 'sprite_count', 'image', 'rect')
    def __init__(self, pos_x: int, pos_y: int, *groups: Group):
        super().__init__(*groups)
        self.type: str = 'Gun'
        self.perma_item: str  = 'GunPerma'
        spritesheet: FileSpriteSheet = SpriteSheet('res/sprite/spritesheet.png')
        self.sprites: Sprite = [spritesheet.get_sprite(0, 0, 11, 7),
                                spritesheet.get_sprite(12, 0, 11, 7),
                                spritesheet.get_sprite(24, 0, 11, 7),
                                spritesheet.get_sprite(36, 0, 11, 7)]
        self.sprite_count: int = 0
        self.image: Sprite = spritesheet.get_sprite(0, 0, 11, 7)
        self.image: Sprite = pygame.transform.scale(self.image, [22, 14])
        self.rect: Rect = pygame.Rect(pos_x, pos_y, 35, 28)

    def Pickup(self)-> Estate:
        return ['HeroGun', True]

    def update(self):
        if self.sprite_count >= len(self.sprites):
            self.sprite_count = 0

        self.image = self.sprites[int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, [44, 28])

        self.sprite_count += 0.075

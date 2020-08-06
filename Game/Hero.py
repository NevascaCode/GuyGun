import pygame
import math
from spritesheet import SpriteSheet
from Bullet import Bullet

class Hero(pygame.sprite.Sprite):
    def __init__(self, shadow, *groups):
        super().__init__(*groups)
        sprite_sheet = SpriteSheet('data/spritesheet.png')
        self.sprites = {'HeroRun':[sprite_sheet.get_sprite(1, 9, 7, 7),
                                   sprite_sheet.get_sprite(11, 9, 7, 7),
                                   sprite_sheet.get_sprite(21, 9, 7, 7),(28, 28)],
                        'HeroGun':[sprite_sheet.get_sprite(32, 22, 11, 9),
                                   sprite_sheet.get_sprite(44, 22, 11, 9),
                                   sprite_sheet.get_sprite(56, 22, 11, 9),(44, 36)]}

        self.animations = {'Gun': False, 'GunPerma': False}

        self.sprite_count = 1
        self.key_down = []
        self.sprite_anim = 'HeroRun'
        self.rotation = 0
        self.idle = 5
        self.image = sprite_sheet.get_sprite(0, 9, 9, 9)
        self.image = pygame.transform.scale(self.image, [28, 28])
        self.rect = pygame.Rect(300, 300, 28, 28)
        self.shadow = shadow.create(self.sprite_anim, self.rect.x, self.rect.y, 8, 3)
        self.shadow.image = pygame.transform.scale(self.shadow.image, (32, 12))

    def update(self):
        if(int(self.sprite_count) >= len(self.sprites[self.sprite_anim])-1):
            self.sprite_count = 0
        self.image = self.sprites[self.sprite_anim][int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, self.sprites[self.sprite_anim][-1])

        self.idle -= 0.5
        if self.idle <= 0:
            self.idle = 0
            self.image = self.sprites[self.sprite_anim][0]
            self.image = pygame.transform.scale(self.image, self.sprites[self.sprite_anim][-1])

        if self.rotation:
            self.image = pygame.transform.flip(self.image, True, False)

        self.shadow.rect.x = self.rect.x-1
        self.shadow.rect.y = self.rect.y+25

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rect.y -= 4
        if(keys[pygame.K_s]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rect.y += 4
        if(keys[pygame.K_a]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rotation = True
            self.rect.x -= 4
        if(keys[pygame.K_d]):
            self.sprite_count += 0.05
            self.rotation = False
            self.idle = 5
            self.rect.x += 4

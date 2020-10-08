import pygame
import math
from src.MyTypes import Rect, Sprite, Speed, Group, Entity
from src.Map import Map
from src.spritesheet import SpriteSheet

class Hero(pygame.sprite.Sprite):
    def __init__(self, shadow: Entity, *groups: Group):
        super().__init__(*groups)
        sprite_sheet = SpriteSheet('res/sprite/spritesheet.png')
        self.sprites: Sprite = {'HeroRun':[sprite_sheet.get_sprite(1, 9, 7, 7),
                                   sprite_sheet.get_sprite(11, 9, 7, 7),
                                   sprite_sheet.get_sprite(21, 9, 7, 7),(28, 28)],
                                'HeroGun':[sprite_sheet.get_sprite(32, 22, 11, 9),
                                   sprite_sheet.get_sprite(44, 22, 11, 9),
                                   sprite_sheet.get_sprite(56, 22, 11, 9),(44, 36)]}

        self.image: Sprite = sprite_sheet.get_sprite(0, 9, 9, 9)
        self.image: Sprite = pygame.transform.scale(self.image, [28, 28])
        self.rect: Rect = pygame.Rect(32*8, 32*8, 28, 28)

        self.sprite_anim: Sprite= 'HeroRun'
        self.animations: dict= {'Gun': False, 'GunPerma': False}

        self.lado_x: Rect = [True,True]
        self.lado_y: Rect = [True,True]

        self.la_x = 0
        self.la_y = 0

        self.speed: int = 5
        self.sprite_count: int = 1

        self.rotation = None

        self.shadow = shadow.create(self.sprite_anim, self.rect.x, self.rect.y, 8, 3)
        self.shadow.image = pygame.transform.scale(self.shadow.image, (32, 12))

    def update(self):
        if(int(self.sprite_count) >= len(self.sprites[self.sprite_anim])-1):
            self.sprite_count = 0
        self.image = self.sprites[self.sprite_anim][int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, self.sprites[self.sprite_anim][-1])

        self.speed -= 0.5
        if self.speed <= 0:
            self.speed = 0
            self.image = self.sprites[self.sprite_anim][0]
            self.image = pygame.transform.scale(self.image, self.sprites[self.sprite_anim][-1])

        if self.rotation:
            self.image = pygame.transform.flip(self.image, True, False)

        self.shadow.rect.x = self.rect.x-1
        self.shadow.rect.y = self.rect.y+25

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            if(self.lado_y[1]):
                self.sprite_count += 0.05
                self.speed = 5
                self.la_y -= 4
                self.rect.y -= 4
                self.subir = True

        if(keys[pygame.K_s]):
            if(self.lado_y[0]):
                self.sprite_count += 0.05
                self.speed = 5
                self.la_y += 4
                self.rect.y += 4
                self.descer = True

        if(keys[pygame.K_a]):
            if(self.lado_x[0]):
                self.sprite_count += 0.05
                self.speed = 5
                self.rotation = True
                self.la_x -= 4
                self.rect.x -= 4

        if(keys[pygame.K_d]):
            if(self.lado_x[1]):
                self.sprite_count += 0.05
                self.rotation = False
                self.speed = 5
                self.la_x += 4
                self.rect.x += 4

        self.lado_x = [True,True]
        self.lado_y = [True,True]
import pygame
from spritesheet import SpriteSheet


class Hero(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        #self.sprites = [pygame.image.load('data/hero_walk1.png'),
        #                pygame.image.load('data/hero_walk2.png')]
        sprite_sheet = SpriteSheet('data/spritesheet.png')
        self.sprites = {'HeroRun':[sprite_sheet.get_sprite(0, 9, 9, 9),
                                   sprite_sheet.get_sprite(10, 9, 9, 9),
                                   sprite_sheet.get_sprite(20, 9, 9, 9),(45,45)],
                        'HeroGun':[sprite_sheet.get_sprite(32, 22, 11, 9),
                                   sprite_sheet.get_sprite(44, 22, 11, 9),
                                   sprite_sheet.get_sprite(56, 22, 11, 9),(55, 45)]}

        self.animations = {'Gun': False, 'GunPerma': False}

        self.sprite_count = 1
        self.key_down = []
        self.sprite_anim = 'HeroRun'
        self.rotation = 0
        self.idle = 5
        self.image = sprite_sheet.get_sprite(0, 9, 9, 9)
        self.image = pygame.transform.scale(self.image, [45, 45])
        self.rect = pygame.Rect(300, 300, 44, 44)

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

        keys = pygame.key.get_pressed()
        #Movimento
        if(keys[pygame.K_w]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rect.y -= 3
        if(keys[pygame.K_s]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rect.y += 3
        if(keys[pygame.K_a]):
            self.sprite_count += 0.05
            self.rotation = True
            self.idle = 5
            self.rect.x -= 3
        if(keys[pygame.K_d]):
            self.sprite_count += 0.05
            self.rotation = False
            self.idle = 5
            self.rect.x += 3

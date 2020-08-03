import pygame
<<<<<<< HEAD
from spritesheet import SpriteSheet
=======
>>>>>>> 473793768308db243b9e52fdaa454dc966de5857

class Gun(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.perma_item = 'GunPerma'
<<<<<<< HEAD
        spritesheet = SpriteSheet('data/spritesheet.png')
        self.sprites = [spritesheet.get_sprite(0, 0, 11, 7),
                        spritesheet.get_sprite(12, 0, 11, 7),
                        spritesheet.get_sprite(24, 0, 11, 7),
                        spritesheet.get_sprite(36, 0, 11, 7)]
        self.sprite_count = 0
        self.image = spritesheet.get_sprite(0, 0, 11, 7)
=======
        self.sprites = [pygame.image.load('data/gun_item.png'),
                        pygame.image.load('data/gun_item2.png'),
                        pygame.image.load('data/gun_item3.png'),
                        pygame.image.load('data/gun_item4.png')]
        self.sprite_count = 0
        self.image = pygame.image.load('data/gun_item.png')
>>>>>>> 473793768308db243b9e52fdaa454dc966de5857
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

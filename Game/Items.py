import pygame

class Gun(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.perma_item = 'GunPerma'
        self.sprites = [pygame.image.load('data/gun_item.png'),
                        pygame.image.load('data/gun_item2.png'),
                        pygame.image.load('data/gun_item3.png'),
                        pygame.image.load('data/gun_item4.png')]
        self.sprite_count = 0
        self.image = pygame.image.load('data/gun_item.png')
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

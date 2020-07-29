import pygame

class Hero(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.sprites = [pygame.image.load('data/hero_walk1.png'),
                        pygame.image.load('data/hero_walk2.png')]
        self.sprite_count = 1
        self.rotation = 0
        self.idle = 5
        self.image = pygame.image.load('data/hero_idle.png')
        self.image = pygame.transform.scale(self.image, [44, 44])
        self.rect = pygame.Rect(300, 300, 7, 7)

    def update(self):
        if(int(self.sprite_count) >= len(self.sprites)) :
            self.sprite_count = 0
        self.image = self.sprites[int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, [44, 44])

        self.idle -= 0.5
        if self.idle <= 0:
            self.idle = 0
            self.image = pygame.image.load('data/hero_idle.png')
            self.image = pygame.transform.scale(self.image, [44, 44])

        if self.rotation:
            self.image = pygame.transform.flip(self.image, True, False)

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_w]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rect.y -= 5
        if(keys[pygame.K_s]):
            self.sprite_count += 0.05
            self.idle = 5
            self.rect.y += 5
        if(keys[pygame.K_a]):
            self.sprite_count += 0.05
            self.rotation = True
            self.idle = 5
            self.rect.x -= 5
        if(keys[pygame.K_d]):
            self.sprite_count += 0.05
            self.rotation = False
            self.idle = 5
            self.rect.x += 5

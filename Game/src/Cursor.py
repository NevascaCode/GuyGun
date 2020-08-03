import pygame

class Cursor(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load('data/neon.png')
        self.image = pygame.transform.scale(self.image, (100, 100))
        #pygame.PixelArray(self.image).replace((255,255,255), (218, 83, 2))
        self.rect = pygame.Rect(5, 5, 5, 5)

    def update(self):
        self.rect.move(pygame.mouse.get_pos())

import pygame
from spritesheet import SpriteSheet
import math
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, *groups):
        super().__init__(*groups)
        spritesheet = SpriteSheet('data/spritesheet.png')
        self.sprites = [spritesheet.get_sprite(31, 12, 5, 5),
                      spritesheet.get_sprite(37, 12, 5, 5),
                      spritesheet.get_sprite(43, 12, 5, 5),
                      spritesheet.get_sprite(49, 12, 5, 5),
                      spritesheet.get_sprite(55, 12, 5, 5),
                      spritesheet.get_sprite(61, 12, 5, 5)]
        self.sprite_count = 0
        self.image = spritesheet.get_sprite(31, 12, 5, 5)
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.mouse = pygame.mouse.get_pos()
        self.rect = pygame.Rect(x_pos, y_pos, 5, 5)
        self.ang = math.atan2(self.rect.x - self.mouse[0], self.rect.y - self.mouse[1])

    def update(self):
        if(self.sprite_count > len(self.sprites)-1):
            self.sprite_count = 0
        self.image = self.sprites[int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.image = pygame.transform.rotate(self.image, 30)
        self.sprite_count += 0.2
        self.rect.x += 0
        self.rect.y += 0

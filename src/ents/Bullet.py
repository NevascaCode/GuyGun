import pygame
from src.MyTypes import Group, Sprite, Rect, Mouse, FileSpriteSheet
from src.spritesheet import SpriteSheet
import math
class Bullet(pygame.sprite.Sprite):
    c_fila = []
    def __init__(self, x_pos: int, y_pos: int, mouse, *groups: Group):
        super().__init__(*groups)

        spritesheet: FileSpriteSheet = SpriteSheet('res/sprite/spritesheet.png')
        self.sprites = [spritesheet.get_sprite(31, 12, 5, 5),
                        spritesheet.get_sprite(37, 12, 5, 5),
                        spritesheet.get_sprite(43, 12, 5, 5),
                        spritesheet.get_sprite(49, 12, 5, 5),
                        spritesheet.get_sprite(55, 12, 5, 5),
                        spritesheet.get_sprite(61, 12, 5, 5)]


        self.sprite_count: int = 0
        self.image: Sprite = spritesheet.get_sprite(31, 12, 5, 5)
        self.image: Sprite = pygame.transform.scale(self.image, (15, 15))
        self.mouse: Mouse = mouse
        self.rect: Rect = pygame.Rect(x_pos, y_pos, 5, 5)

        self.pos_x: int = x_pos
        self.pos_y: int = y_pos

        self.ang: float = math.atan2(self.mouse[0] - self.rect.center[0], self.mouse[1] - self.rect.center[1]) - math.pi / 2
        self.ang_x: float = math.cos(self.ang) * 5
        self.ang_y: float = math.sin(self.ang) * 5

    def update(self):

        if(self.sprite_count > len(self.sprites)-1):
            self.sprite_count = 0
        self.image = self.sprites[int(self.sprite_count)]
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.sprite_count += 0.2

        #Movimento da bala
        self.pos_x += self.ang_x
        self.pos_y -= self.ang_y

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y


        #Kill
        '''if(self.rect.x < 0 or self.rect.x > 514 or self.rect.y < 0 or self.rect.y > 512):
            self.kill()'''

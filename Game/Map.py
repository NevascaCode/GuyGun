import pygame
from spritesheet import SpriteSheet
from Items import Gun
from Enemy import Enemy

class Map(object):
    def __init__(self):
        self.tiles = WorldMapSprite()
        map = SpriteSheet('data/spritesheet.png').get_sprite(112,16,16,16)
        self.map_array_block = pygame.PixelArray(map).extract((255,255,255))
        self.map_array_items = pygame.PixelArray(map).extract((255, 0, 0))
        self.map_array_enemys = pygame.PixelArray(map).extract((0, 255, 0))
    def create_level(self, *groups):
        for y in range(0, 16):
            for x in range(0, 16):
                if(self.map_array_block[y][x] == -1):
                    self.tiles.ColocaBloco(y*32, x*32, 'Block', groups[0])
                if(self.map_array_items[y][x] == -1):
                    Gun(x*32, y*32, groups[1])
                if(self.map_array_enemys[y][x] == -1):
                    Enemy(x*32, y*32, groups[2])

class WorldMapSprite(object):
    def __init__(self):
        image = SpriteSheet('data/spritesheet.png')
        self.tiles = {'Block': image.get_sprite(78, 0, 18, 18)}
    def ColocaBloco(self, pos_x, pos_y, tiless, *groups):
        tile = pygame.sprite.Sprite(groups[0])
        tile.image = self.tiles[tiless]
        tile.image = pygame.transform.scale(tile.image, (36, 36))
        tile.rect = pygame.Rect(pos_x, pos_y, 36, 36)

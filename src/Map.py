import pygame
from .MyTypes import Tile, EntityLevel, Tile, Level, Group, Sprite, Rect
from src.spritesheet import SpriteSheet
from .ents.Items import Gun
from .ents.Enemy import Enemy

class Map(object):
    def __init__(self):
        self.tiles = WorldMapSprite()
        map = SpriteSheet('res/sprite/spritesheet.png').get_sprite(105, 9, 47, 47)
        self.map_array_block_wall: TileLevel = pygame.PixelArray(map).extract((255,255,255))
        self.map_array_items: EntityLevel = pygame.PixelArray(map).extract((255, 0, 0))
        self.map_array_enemys: EntityLevel = pygame.PixelArray(map).extract((0, 255, 0))

    def create_level(self, *groups: Group)-> Level:
        for y in range(0, 47):
            for x in range(0, 47):
                if(self.map_array_block_wall[y][x] == -1):
                    self.tiles.ColocaBloco(y*32, x*32, 'Block', groups[0])
                if(self.map_array_items[y][x] == -1):
                    Gun(y*32, x*32, groups[1])
                if(self.map_array_enemys[y][x] == -1):
                    Enemy(x*32, y*32, groups[2])
                self.tiles.ColocaBloco(y*32, x*32, 'Floor', groups[3])

class WorldMapSprite(object):
    def __init__(self):
        image = SpriteSheet('res/sprite/spritesheet.png')
        self.tiles = {'Block': image.get_sprite(78, 0, 18, 18),
                      'Floor': image.get_sprite(77, 66, 18, 18)}

    def ColocaBloco(self, pos_y: int, pos_x: int, image: Sprite, *groups: Group)-> Tile:
        tile: Tile = pygame.sprite.Sprite(groups[0])
        tile.image = self.tiles[image]
        tile.image = pygame.transform.scale(tile.image, (36, 36))
        tile.rect= pygame.Rect(pos_y, pos_x, 36, 36)

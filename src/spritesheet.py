import pygame
from .MyTypes import FileSpriteSheet, Sprite

class SpriteSheet:
    def __init__(self, file: FileSpriteSheet):
        self.sprite_sheet = pygame.image.load(file)

    def get_sprite(self, x: int, y: int, width: int, height: int)-> Sprite:
        image: Sprite = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

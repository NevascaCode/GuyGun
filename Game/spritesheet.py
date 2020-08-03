import pygame

class SpriteSheet:
    def __init__(self, file):
        self.sprite_sheet = pygame.image.load(file)

    def get_sprite(self, x, y, width, height):
        image = pygame.Surface((width, height), pygame.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        return image

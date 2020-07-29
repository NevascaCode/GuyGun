import pygame
from Hero import Hero


pygame.init()

tela = pygame.display.set_mode([600,600])

hero_group = pygame.sprite.Group()
Hero = Hero(hero_group)

fps_clock = pygame.time.Clock()

GAMELOOP = True
while GAMELOOP:
    fps_clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAMELOOP = False

    tela.fill([68, 52, 191])

    hero_group.draw(tela)
    hero_group.update()

    pygame.display.update()

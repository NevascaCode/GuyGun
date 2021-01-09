import pygame

from .MyTypes import Sprite, Image, Level, Clock, Group, Entity, NewGame, RunGame
from .ents.Hero import Hero
from .ents.Items import Gun
from .ents.Bullet import Bullet
from .Map import Map


class Game(object):
    __slots__ = ('tela_x', 'tela_y', 'mapa', 'tela', 'camera', 'enemys_group', 'tiles_group', 'floor_group', 'fps_clock', 'GAMELOOP', 'bullet_group',
                 'items_group','hero_group', 'Hero', 'fps_clock','para_x', 'para_y')
    def __init__(self):
        pygame.init()
        self.mapa: Level = Map()
        self.tela = pygame.display.set_mode([514, 512], flags= pygame.HWSURFACE | pygame.DOUBLEBUF )
        self.camera = pygame.Surface([1504, 1504])
        pygame.display.set_caption('GuyGun')
        self.fps_clock: Clock = pygame.time.Clock()
        self.tela_x = 514
        self.tela_y = 512

        self.para_x = 514
        self.para_y = 512

        self.GAMELOOP: bool = True

    def new(self)-> NewGame:
        self.enemys_group: Group = pygame.sprite.Group()
        self.tiles_group: Group = pygame.sprite.Group()
        self.bullet_group: Group = pygame.sprite.Group()
        self.items_group: Group = pygame.sprite.Group()
        self.hero_group: Group = pygame.sprite.Group()
        self.floor_group = pygame.sprite.Group()
        self.Hero: Player = Hero(self.hero_group)
        self.mapa.create_level(self.tiles_group, self.items_group, self.enemys_group, self.floor_group)

    def run(self)-> RunGame:
        self.new()
        while self.GAMELOOP:
            self.events()
            self.update()
            self.colisions()
            self.draw()
            self.fps_clock.tick(60)

    def events(self)-> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GAMELOOP = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and self.Hero.animations['GunPerma']:
                    self.Hero.animations['Gun'] = not self.Hero.animations['Gun']
                    if self.Hero.animations['Gun'] and self.Hero.animations['GunPerma']:
                        self.Hero.sprite_anim: Sprite = 'HeroGun'
                    else:
                        self.Hero.sprite_anim: Sprite = 'HeroRun'
                    self.hero_group.update()
            if event.type == pygame.MOUSEBUTTONDOWN and self.Hero.animations['Gun'] == True:
                Bullet(self.Hero.rect.x, self.Hero.rect.y, (pygame.mouse.get_pos()[0]+(self.para_x), pygame.mouse.get_pos()[1]+(self.para_y)), self.bullet_group)

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_d]):
            self.Hero.get_key(keys)

    def draw(self)-> None:
        self.floor_group.draw(self.camera)
        self.hero_group.draw(self.camera)
        self.enemys_group.draw(self.camera)
        self.bullet_group.draw(self.camera)
        self.items_group.draw(self.camera)
        self.tiles_group.draw(self.camera)


        self.para_x = self.Hero.rect.x-257
        self.para_y = self.Hero.rect.y-256
        self.limitar_camera()
        self.tela.blit(self.camera, (0,0), [self.para_x, self.para_y, self.tela_x, self.tela_y])


    def limitar_camera(self):
        if self.Hero.rect.x+257 >= 1504:
            self.para_x = 1504 - self.tela_x
        if self.Hero.rect.x-257 <= 0:
            self.para_x = 0

        if self.Hero.rect.y+257 >= 1504:
            self.para_y = 1504 - self.tela_y
        if self.Hero.rect.y-257 <= 0:
            self.para_y = 0

    def update(self)-> None:
        self.hero_group.update()
        self.enemys_group.update()
        self.bullet_group.update()
        self.items_group.update()
        pygame.display.flip()

    def colisions(self)-> None:
        for item in pygame.sprite.spritecollide(self.Hero, self.items_group, True):
            if item.type == 'Gun':
                self.Hero.animations['Gun']: Sprite = item.Pickup()[1]
                self.Hero.animations[item.perma_item] = item.Pickup()[1]
                self.Hero.sprite_anim: Sprite = item.Pickup()[0]

        for tile in pygame.sprite.spritecollide(self.Hero, self.tiles_group, False):
            if(tile.rect.left == self.Hero.rect.right-4):
                self.Hero.rect.x -= 4
                self.Hero.lado_x = [True, False]
                self.Hero.lado_y = [True, True]

            if(tile.rect.right == self.Hero.rect.left+4):
                self.Hero.rect.x += 4
                self.Hero.lado_x = [False, True]
                self.Hero.lado_y = [True, True]

            if(tile.rect.bottom == self.Hero.rect.top+4):
                self.Hero.rect.y += 4
                self.Hero.lado_x = [True, True]
                self.Hero.lado_y = [True, False]

            if(tile.rect.top == self.Hero.rect.bottom-4):
                self.Hero.rect.y -= 4
                self.Hero.lado_x = [True, True]
                self.Hero.lado_y = [False, True]

        for colisao in pygame.sprite.groupcollide(self.enemys_group, self.bullet_group, False, True):
            colisao.lifes -= 1
            print(colisao.lifes)

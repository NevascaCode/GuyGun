import pygame
from Shadow import Shadow
from Hero import Hero
from Items import Gun
from Bullet import Bullet
from Map import Map

class Game(object):
    def __init__(self):
        pygame.init()
        self.mapa = Map()
        self.tela = pygame.display.set_mode([514, 512])
        pygame.display.set_caption('BlockDeath')
        self.fps_clock = pygame.time.Clock()
        self.GAMELOOP = True

    def new(self):
        self.enemys_group = pygame.sprite.Group()
        self.tiles_group = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.items_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()
        self.shadow_group = pygame.sprite.Group()
        self.shadow = Shadow(self.shadow_group)
        self.Hero = Hero(self.shadow, self.hero_group)
        self.mapa.create_level(self.tiles_group, self.items_group, self.enemys_group)

    def run(self):
        self.new()
        while self.GAMELOOP:
            self.fps_clock.tick(60)
            self.events()
            self.draw()
            self.update()
            self.colisions()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GAMELOOP = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1 and self.Hero.animations['GunPerma']:
                    self.Hero.animations['Gun'] = not self.Hero.animations['Gun']
                    if self.Hero.animations['Gun'] and self.Hero.animations['GunPerma']:
                        self.Hero.sprite_anim = 'HeroGun'
                    else:
                        self.Hero.sprite_anim = 'HeroRun'
            if event.type == pygame.MOUSEBUTTONDOWN and self.Hero.animations['Gun'] == True:
                Bullet(self.Hero.rect.x, self.Hero.rect.y, self.bullet_group)


    def draw(self):
        self.tela.fill([36, 48, 65])
        self.shadow_group.draw(self.tela)
        self.enemys_group.draw(self.tela)
        self.bullet_group.draw(self.tela)
        self.items_group.draw(self.tela)
        self.hero_group.draw(self.tela)
        self.tiles_group.draw(self.tela)

    def update(self):
        self.shadow_group.update()
        self.enemys_group.update()
        self.bullet_group.update()
        self.items_group.update()
        self.hero_group.update()
        pygame.display.update()

    def colisions(self):
        for item in pygame.sprite.spritecollide(self.Hero, self.items_group, True):
            if item.type == 'Gun':
                self.Hero.animations['Gun'] = item.Pickup()[1]
                self.Hero.animations[item.perma_item] = item.Pickup()[1]
                self.Hero.sprite_anim = item.Pickup()[0]
        for tile in pygame.sprite.spritecollide(self.Hero, self.tiles_group, False):
            print(f'-Tile:{tile.rect.y+28} \n -Hero:{self.Hero.rect.y-4}')
            if(tile.rect.x+4 == self.Hero.rect.x+28):
                self.Hero.rect.x -= 4
            if(tile.rect.x+28 == self.Hero.rect.x-4):
                self.Hero.rect.x += 4
            if(tile.rect.y+28 == self.Hero.rect.y-4):
                self.Hero.rect.y += 4
            if(tile.rect.y+4 == self.Hero.rect.y+28):
                self.Hero.rect.y -=4



game = Game()
if game.GAMELOOP:
    game.run()

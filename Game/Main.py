import pygame
from Hero import Hero
from Items import Gun

class Game(object):
    def __init__(self):
        pygame.init()
        self.tela = pygame.display.set_mode([600,600])
        self.fps_clock = pygame.time.Clock()
        self.GAMELOOP = True

    def new(self):
        self.items_group = pygame.sprite.Group()
        self.hero_group = pygame.sprite.Group()
        self.Hero = Hero(self.hero_group)
        Gun(self.items_group)

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
                if event.key == pygame.K_1:
                    if self.Hero.animations['Gun'] and self.Hero.animations['GunPerma']:
                        self.Hero.sprite_anim = 'HeroGun'
                    else:
                        self.Hero.sprite_anim = 'HeroRun'
                    self.Hero.animations['Gun'] = not self.Hero.animations['Gun']

    def draw(self):
        self.tela.fill([68, 52, 191])
        self.items_group.draw(self.tela)
        self.hero_group.draw(self.tela)

    def update(self):
        self.items_group.update()
        self.hero_group.update()
        pygame.display.update()


    def colisions(self):
        for item in pygame.sprite.spritecollide(self.Hero, self.items_group, True):
            self.Hero.animations[item] = item.Pickup()[1]
            self.Hero.animations[item.perma_item] = item.Pickup()[1]
            self.Hero.sprite_anim = item.Pickup()[0]

game = Game()
if game.GAMELOOP:
    game.run()

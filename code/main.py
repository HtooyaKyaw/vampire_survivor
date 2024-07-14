from settings import *
from player import Player
import pygame
from sprites import *
from random import randint
from pytmx.util_pygame import load_pygame
from groups import AllSprites

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Survivor')
        self.clock = pygame.time.Clock()
        self.running = True

        #groups
        self.all_sprites = AllSprites()
        self.collision_sprites = pygame.sprite.Group()

        self.setup()

        # #sprites
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        # for i in range(6):
        #     x,y = randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT)
        #     w,h = randint(60,100),randint(50,100)
        #     Collision_sprite((x,y),(w,h),(self.all_sprites, self.collision_sprites))

    def setup(self):
        map = load_pygame(join('../data','maps','world.tmx'))
        for x,y,image in map.get_layer_by_name('Ground').tiles():
            Sprite((x* TILE_SIZE,y*TILE_SIZE),image,self.all_sprites)
        for obj in map.get_layer_by_name('Objects'):
            Collision_sprite((obj.x,obj.y),obj.image,(self.all_sprites,self.collision_sprites))

        for obj in map.get_layer_by_name('Collisions'):
            Collision_sprite((obj.x,obj.y),pygame.Surface((obj.width,obj.height)),(self.collision_sprites))
    def run(self):
        while self.running:
            #dt
            dt = self.clock.tick() / 1000
            #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    self.running = False
            #update
            self.all_sprites.update(dt)
            #draw
            self.display_surface.fill((0, 0, 0))
            self.all_sprites.draw()
            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()

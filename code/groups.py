from settings import *

class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display = pygame.display.get_surface()
        # self.groups = all_sprites
        # all_sprites.add(self)

    def draw(self):
        for sprite in self:
            self.display.blit(sprite.image, sprite.rect.topleft + pygame.Vector2(500, 100))

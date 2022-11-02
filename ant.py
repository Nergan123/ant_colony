from pygame import sprite, Surface


class Ant(sprite.Sprite):
    def __init__(self):
        super(Ant, self).__init__()
        self.surf = Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

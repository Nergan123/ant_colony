from pygame import sprite, Surface


class Spawn(sprite.Sprite):
    def __init__(self, x, y):
        super(Spawn, self).__init__()
        self.surf = Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.x = x
        self.y = y

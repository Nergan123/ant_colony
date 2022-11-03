from pygame import sprite, Surface


class Food(sprite.Sprite):
    def __init__(self, x, y):
        super(Food, self).__init__()
        self.surf = Surface((10, 10))
        self.surf.fill((255, 0, 255))
        self.x = x
        self.y = y

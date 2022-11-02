import pygame
from pygame.locals import *
from ant import Ant
from phero_map import Phero_map


class App:
    def __init__(self, width=200, height=200, fps=24):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.ant = Ant(100, 100)
        self.phero_map = Phero_map(width, height)

    def run(self):
        while self.running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.ant.choose_next(self.phero_map.canvas)
            self.screen.blit(self.ant.surf, (self.ant.pos_x, self.ant.pos_y))
            pygame.display.flip()

        pygame.quit()

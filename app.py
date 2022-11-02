import pygame
from pygame.locals import *
from ant import Ant


class App:
    def __init__(self, width=800, height=600, fps=24):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.ant = Ant()

    def run(self):
        while self.running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.blit(self.ant.surf, self.ant.rect)
            pygame.display.flip()

        pygame.quit()

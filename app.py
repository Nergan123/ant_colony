import pygame
from pygame.locals import *
from ant import Ant
from phero_map import Phero_map
from spawn import Spawn
from food import Food


class App:
    def __init__(self, width=200, height=200, fps=24, ant_num=10):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.spawn = Spawn(100, 100)
        self.food = Food(100, 20)
        self.phero_map = Phero_map(width, height)
        self.ants = []
        for i in range(ant_num):
            self.ants.append(Ant(100, 100))

    def run(self):
        while self.running:
            self.clock.tick(self.fps)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))
            self.phero_map.update_phero(1.01)

            for ant in self.ants:
                ant.choose_next(self.phero_map.canvas)
                ant.check_state(self.spawn.x, self.spawn.y, self.food.x, self.food.y)
                self.screen.blit(ant.surf, (ant.pos_y, ant.pos_x))

                if ant.state == 'from':
                    self.phero_map.update_from_food(ant.pos_y, ant.pos_x, 0.1)
                elif ant.state == 'to':
                    self.phero_map.update_to_food(ant.pos_y, ant.pos_x, 0.1)

            z = self.phero_map.get_map()
            surf = pygame.surfarray.make_surface(z)
            self.screen.blit(surf, (0, 0))
            self.screen.blit(self.spawn.surf, (self.spawn.x, self.spawn.y))
            self.screen.blit(self.food.surf, (self.food.x, self.food.y))

            pygame.display.flip()

        pygame.quit()

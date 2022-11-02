from pygame import sprite, Surface
import numpy as np
import random


class Ant(sprite.Sprite):
    def __init__(self, x=10, y=10):
        super(Ant, self).__init__()
        self.surf = Surface((1, 1))
        self.surf.fill((255, 255, 255))
        self.pos_x = x
        self.pos_y = y
        self.state = 'to'
        self.alpha = 0.5

    def choose_next(self, phero_map):
        if self.state == 'to':
            summ = 0
            for x in range(-1, 1):
                for y in range(-1, 1):
                    summ += phero_map[self.pos_x+x, self.pos_y+y, 0]

            if summ == 0:
                summ = 0.000001

            prob = np.zeros((3, 3))
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        prob[x+1, y+1] = 0
                    else:
                        val = phero_map[self.pos_x+x, self.pos_y+y, 0]
                        prob[x+1, y+1] = val/summ

            print(prob)
            val = random.uniform(0, 1)
            x, y = self.find_nearest(prob, val)
            print(f'x:{x-1} y:{y-1}')
            self.pos_x += x-1
            self.pos_y += y-1

    @staticmethod
    def find_nearest(array, value):
        print(value)
        val_old = 100
        row_ind_out = 0
        col_ind_out = 0
        for col_ind, row in enumerate(array):
            for row_ind, val in enumerate(row):
                if abs(val - value) < val_old:
                    val_old = abs(val - value)
                    row_ind_out = row_ind
                    col_ind_out = col_ind

        return row_ind_out, col_ind_out

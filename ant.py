from pygame import sprite, Surface
import numpy as np
import random
import itertools


class Ant(sprite.Sprite):
    def __init__(self, x=10, y=10):
        super(Ant, self).__init__()
        self.surf = Surface((1, 1))
        self.surf.fill((255, 255, 255))
        self.pos_x = x
        self.pos_y = y
        self.pos_x_prev = x
        self.pos_y_prev = y
        self.state = 'to'
        self.alpha = 0.5

    def choose_next(self, phero_map):
        if self.state == 'to':
            self.get_next_pos(1, phero_map)
        else:
            self.get_next_pos(0, phero_map)

    def get_next_pos(self, layer, phero_map):

        prob = np.zeros((11, 11))
        for x in range(-5, 6):
            for y in range(-5, 6):
                if x == 0 and y == 0:
                    prob[x+5, y+5] = 0
                else:
                    prob[x+5, y+5] = phero_map[self.pos_y+y, self.pos_x+x, layer]

        val = random.uniform(0, 1)
        x, y = self.find_nearest(prob, val)
        while self.pos_x + x - 5 == self.pos_x_prev and self.pos_y + y - 5 == self.pos_y_prev:
            val = random.uniform(0, 1)
            x, y = self.find_nearest(prob, val)

        self.pos_x_prev = self.pos_x
        self.pos_y_prev = self.pos_y
        self.pos_x += x-5
        self.pos_y += y-5

        if self.pos_x < 6:
            self.pos_x = 6
        if self.pos_y < 6:
            self.pos_y = 6

        if self.pos_x > 194:
            self.pos_x = 194
        if self.pos_y > 194:
            self.pos_y = 194

    def find_nearest(self, array, value):
        array = self.cumulative_sum(array)
        for col_ind, row in enumerate(array):
            for row_ind, val in enumerate(row):
                if val >= value:
                    return col_ind, row_ind

        return 5, 5

    def check_state(self, spawn_y, spawn_x, food_y, food_x):
        if self.state == 'to':
            if (food_x < self.pos_x < food_x + 20) and (food_y < self.pos_y < food_y + 20):
                self.state = 'from'
        else:
            if (spawn_x < self.pos_x < spawn_x + 20) and (spawn_y < self.pos_y < spawn_y + 20):
                self.state = 'to'

    @staticmethod
    def cumulative_sum(array_in):
        prev_val = 0
        for col_ind, row in enumerate(array_in):
            for row_ind, val in enumerate(row):
                array_in[col_ind, row_ind] = array_in[col_ind, row_ind] + prev_val
                prev_val = array_in[col_ind, row_ind]

        output_res = array_in/prev_val

        return output_res

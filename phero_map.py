import numpy as np


class Phero_map:
    def __init__(self, width=800, height=600):
        self.canvas = np.random.uniform(0, 1, (width, height, 2))   # zeros((width, height, 2))

    def update_to_food(self, x, y, val):
        self.canvas[x, y, 0] = val

    def update_from_food(self, x, y, val):
        self.canvas[x, y, 1] = val

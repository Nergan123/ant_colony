import numpy as np


class Phero_map:
    def __init__(self, width=800, height=600):
        self.canvas = np.random.uniform(0, 0.01, (width, height, 3))   #
        self.canvas[:, :, 2] = 0

    def update_to_food(self, y, x, val):
        self.canvas[x, y, 0] = self.canvas[x, y, 0] + val
        if self.canvas[x, y, 0] > 1:
            self.canvas[x, y, 0] = 1

    def update_from_food(self, y, x, val):
        self.canvas[x, y, 1] = self.canvas[x, y, 1] + val
        if self.canvas[x, y, 1] > 1:
            self.canvas[x, y, 1] = 1

    def get_map(self):
        output = np.zeros(self.canvas.shape)
        output[:, :, 0] = self.scale(self.canvas[:, :, 0])
        output[:, :, 1] = self.scale(self.canvas[:, :, 1])
        output[:, :, 2] = np.zeros(self.canvas.shape[0:1])
        output = np.swapaxes(output, 0, 1)
        return output.astype(np.uint8)

    @staticmethod
    def scale(x, out_range=(0, 255)):
        domain = np.min(x), np.max(x)
        y = (x - (domain[1] + domain[0]) / 2) / (domain[1] - domain[0])
        return y * (out_range[1] - out_range[0]) + (out_range[1] + out_range[0]) / 2

    def update_phero(self, val):
        self.canvas[:, :, 0] = self.canvas[:, :, 0]/val
        self.canvas[:, :, 1] = self.canvas[:, :, 1]/val

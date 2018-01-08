from surface.Surface import Surface
import numpy as np


class Bed(object):
    def __init__(self):
        super().__init__()
        self.random_wave_surface = Surface((100, 100), 5, 0.3).normal(0)[:, :, 0]

    def new_random_surface(self):
        self.random_wave_surface = Surface((100, 100), 5, 0.3).normal(0)[:, :, 0]

    def sphere(shape, radius, position):
        # assume shape and position are both a 3-tuple of int or float
        # the units are pixels / voxels (px for short)
        # radius is a int or float in px
        semisizes = (radius,) * 3

        # genereate the grid for the support points
        # centered at the position indicated by position
        grid = [slice(-x0, dim - x0) for x0, dim in zip(position, shape)]
        position = np.ogrid[grid]
        # calculate the distance of all points from `position` center
        # scaled by the radius
        arr = np.zeros(shape, dtype=float)
        for x_i, semisize in zip(position, semisizes):
            arr += (np.abs(x_i / semisize) ** 2)
        # the inner part of the sphere will have distance below 1
        return arr <= 1.0

    def bed_depths(self, shape):
        depths = np.ndarray([100, 100], dtype=np.float32)
        if shape == "straight":
            for i in range(depths.shape[0]):
                for j in range(depths.shape[1]):
                    if i <= 19:
                        depths[i][j] = 1
                    elif i >= 80:
                        depths[i][j] = 5
                    else:
                        depths[i][j] = (i - 20) * 4 / 58 + 1

        if shape == "random":
            depths = self.random_wave_surface

        if shape == "linspace":
            depths = np.linspace(-1.5, -1.4, 10000, dtype=np.float32).reshape([100, 100])

        if shape == "beach":
            depths = np.linspace(-0.1, 0, 10000, dtype=np.float32).reshape([100, 100])

        if shape == "sky":
            for i in range(depths.shape[0]):
                for j in range(depths.shape[1]):
                    print((2 - ((i - 50) / 50) ** 2 - ((j - 50) / 50) ** 2))
                    depths[i][j] = ((20 - ((i - 50) / 50) ** 2 - ((j - 50) / 50) ** 2) ** 0.5 + 0.0000000000001) - 4.36
            print(depths)
            return depths

        return depths - 0.3

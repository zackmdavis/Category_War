import functools
import itertools

import matplotlib.pyplot as plot
from matplotlib.colors import ListedColormap
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import array
from numpy.random import normal
from sklearn import svm


class Entity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def trait_vector(self):
        return [self.x, self.y, self.z]

    @classmethod
    def generate_a(cls):
        x = normal(4, 1)
        y = normal(4, 1)
        z = normal(4, 1)
        return cls(x, y, z)

    @classmethod
    def generate_b(cls):
        x = normal(6, 1)
        y = normal(6, 1)
        z = normal(6, 1)
        return cls(x, y, z)

    def project_x(self):
        return self.__class__(self.x, 0, 0)

    def project_y(self):
        return self.__class__(0, self.y, 0)

    def project_z(self):
        return self.__class__(0, 9, self.z)


def plot_projection_lines(p, axes, color):
    z_drop = np.linspace(0, p.z, 1000)
    x_drop = [p.x for _ in range(1000)]
    y_drop = [p.y for _ in range(1000)]
    axes.plot3D(x_drop, y_drop, z_drop, color)

    zline2 = [0 for _ in range(1000)]
    xline2 = np.linspace(0, p.x, 1000)
    yline2 = [p.y for _ in range(1000)]
    axes.plot3D(xline2, yline2, zline2, color)

    zline3 = [0 for _ in range(1000)]
    xline3 = [p.x for _ in range(1000)]
    yline3 = np.linspace(0, p.y, 1000)
    axes.plot3D(xline3, yline3, zline3, color)


def letter_index(letter):
    return {'x': 0, 'y': 1, 'z': 2}[letter]


def plot_offside_interval(lo, hi, axis, axes, color):
    offsides = [[-0.4 for _ in range(1000)] for _ in range(3)]
    segment = np.linspace(lo, hi, 1000)
    offsides[letter_index(axis)] = segment
    if axis == 'z':
        offsides[1] = [8.6 for _ in range(1000)]
    args = offsides + [color]
    axes.plot3D(*args)


def my_plot():
    group_size = 18

    p1 = [Entity.generate_b() for _ in range(group_size)]
    p2 = [Entity.generate_a() for _ in range(group_size)]

    p1x = [p.project_x() for p in p1]
    p2x = [p.project_x() for p in p2]

    p1y = [p.project_y() for p in p1]
    p2y = [p.project_y() for p in p2]

    p1z = [p.project_z() for p in p1]
    p2z = [p.project_z() for p in p2]

    xleast_p1 = min(p1, key=lambda p: p.x)
    xmost_p2 = max(p2, key=lambda p: p.x)

    yleast_p1 = min(p1, key=lambda p: p.y)
    ymost_p2 = max(p2, key=lambda p: p.y)

    zleast_p1 = min(p1, key=lambda p: p.z)
    zmost_p2 = max(p2, key=lambda p: p.z)

    entities = p1 + p2 + p1x + p2x + p1y + p2y + p1z + p2z
    p = array([e.trait_vector() for e in entities])

    target = list(
        functools.reduce(
            itertools.chain,
            [itertools.repeat(i, group_size) for i in range(1, 9)]
        )
    )

    figure = plot.figure(figsize=(6, 5))
    axes = Axes3D(figure)

    axes.scatter(p[:, 0], p[:, 1], p[:, 2],
                 c=target,
                 cmap=ListedColormap(
                     ["#0000f0", "#f03c00",
                      "#0000a0",  "#a02800",
                      "#0000a0",  "#a02800",
                      "#0000a0",  "#a02800"]
                 )
    )

    plot_offside_interval(xleast_p1.x, xmost_p2.x, 'x', axes, "#101010")
    plot_offside_interval(yleast_p1.y, ymost_p2.y, 'y', axes, "#101010")
    plot_offside_interval(zleast_p1.z, zmost_p2.z, 'z', axes, "#101010")

    plot_projection_lines(xleast_p1, axes, "#8080f0")
    plot_projection_lines(xmost_p2, axes, "#f09040")

    plot.show()


if __name__ == "__main__":
    my_plot()

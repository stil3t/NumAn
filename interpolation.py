import csv
from math import *
import numpy as np

from matplotlib import pyplot as plt


def generateDataInRange(func, start, stop, step, disp=0, buildPlot=False):
    """Создает табличное представление функции func на отрезке [start; stop] с шагом step.
       Можно добавить шумы и построить график"""

    X = np.arange(start, stop + step / 2, step)
    Y = func(X) + (np.random.rand(len(X)) - .5) * disp * 2

    if buildPlot:
        plt.plot(X, Y, 'o')
        plt.title("Plot of generated function")
        # plt.xlabel('X')
        # plt.ylabel('Y')
        plt.show()

    return {X[i]: Y[i] for i in range(len(X))}


def lagrange(X, Y):
    res = []
    def denominator(X, n):
        res = 1
        for i in range(len(X)):
            if i == n:
                continue
            res *= (X[n] - X[i])
        return res

    # for i in range(len(X)):


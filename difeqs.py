import csv
from math import *
import numpy as np
import re


def EuCau(f, x0, y0, a, b, accuracy=.001):

    assert a < b
    x = np.arange(x0, b, accuracy)
    y = [y0, y0 + accuracy * f(x0, y0)]

    for i in range(2, int((b-x0)/accuracy)):
        yy = y[i-1] + accuracy*f(x[i-1], y[i-1])
        y.append(y[i-1] + (accuracy/2)*(f(x[i-1], y[i-1]) + f(x[i], yy)))

    return x, y


def RK4(f, x0, y0, a, b, accuracy=.001):

    assert a < b
    x = np.arange(x0, b, accuracy)
    y = [y0]

    for i in range(1, int((b-x0)/accuracy)):
        try:
            k1 = accuracy * f(x[i-1], y[i-1])
            k2 = accuracy * f(x[i-1] + accuracy/2, y[i-1] + k1/2)
            k3 = accuracy * f(x[i-1] + accuracy/2, y[i-1] + k2/2)
            k4 = accuracy * f(x[i], y[i-1] + k3)
        except ZeroDivisionError:
            y.append(y[i - 1])
        else:
            y.append(y[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6.)
    return x, y


def RK4s(fs, x0, y0s, a=0, b=1, accuracy=.001):

    x = np.arange(x0, b, accuracy)
    y = [y0s]

    for i in range(1, int((b-x0)/accuracy)):
        y_curr = []
        for fno, f in enumerate(fs):
            try:
                k1 = accuracy * f(x[i - 1], *y[i-1])
                k2 = accuracy * f(x[i - 1] + accuracy / 2, *[y[i-1][j] + k1 / 2 for j in range(len(y0s))])
                k3 = accuracy * f(x[i - 1] + accuracy / 2, *[y[i-1][j] + k2 / 2 for j in range(len(y0s))])
                k4 = accuracy * f(x[i], *[y[i-1][j] + k3 for j in range(len(y0s))])
            except ZeroDivisionError:
                y_curr.append((y[i-1][fno]))
            else:
                y_curr.append(y[i - 1][fno] + (k1 + 2 * k2 + 2 * k3 + k4) / 6.)
        y.append(y_curr)
    return x, y


def Comp(a, b):

    assert len(a) == len(b)
    er = 0
    for i in range(len(a)):
        er += (a[i]-b[i])**2

    return er

import csv
from math import *
import numpy as np
import re


def generate(n, m, min_value=-10., max_value=10.):
    """Функция генерирует матрицу, в которой n строк и m столбцов.
       Можно задать минимальное и максимальное значения элементов/"""

    assert min_value < max_value, 'Минимальное значение должно быть меньше максимального значения'

    dispersion = max_value - min_value
    x = np.random.random(n * m) * dispersion + min_value
    x = x.reshape(n, m)

    return Matrix(x)


def ints(n, m, min_value=-10, max_value=10):
    """Функция генерирует матрицу целых чисел, в которой n строк и m столбцов.
       Можно задать минимальное и максимальное значения элементов."""

    assert min_value < max_value, 'Минимальное значение должно быть меньше максимального значения'

    x = np.random.randint(min_value, max_value + 1, n * m)
    x = x.reshape(n, m)

    return Matrix(x)


def inp(fast=False):
    """Ввод матрицы пользователем.
    Сначала вводится размер, затем каждый элемент. В случае отмены, нужно ввести 'exit'.
    Также элементами могут быть строки, состоящие из букв, символа _, и цифр (но не на первой позиции)
    fast для ускоренного ввода"""

    number_of_rows = int(input("Введите число строк: "))
    number_of_elements = int(input("Введите число стобцов: "))
    matrix = []

    if fast:
        for n in range(number_of_rows):
            row = [float(i) for i in input().split()]
            assert len(row) == number_of_elements, 'Неверный ввод'
            matrix.append(row)
        return Matrix(matrix)

    else:
        print("Далее нужно ввести элементы матрицы.\n"
              "  Первый индекс - номер строки, второй - элемент строки.\n"
              "  Для выхода введите 'stop'")
        for n in range(number_of_rows):
            row = []
            for m in range(number_of_elements):

                elem = input("a[{}][{}]".format(n, m))

                if elem == 'stop':
                    raise Exception('Остановлено пользователем')

                else:
                    try:
                        row.append(float(elem))
                    except ValueError:
                        assert re.fullmatch(r'[-]?[a-zA-Zа-яА-Я]', elem), 'Неверный ввод'
                        row.append(elem)

            matrix.append(row)
        return Matrix(matrix)


def red(matrix, y, x):
    """Возвращает матрицу с удаленной строкой y и столбцом x.
    Нужно для вычисления определителя больших матриц"""

    res = []

    for nn in range(n):
        if nn == y: continue
        current_row = []
        for mm in range(m):
            if mm == x: continue
            current_row.append(matrix[nn][mm])
        res.append(current_row)
    return res


def matrixShape(matrix):
    try:
        n = len(matrix)
        m = len(matrix[0])
    except:
        print("list of lists expected")
    return n, m


def det(matrix):
    """Нахождение определителя квадратной матрицы, рекурсия до матрицы рангом 3"""
    assert matrixShape(matrix)[0] == matrixShape(matrix)[1], 'Матрица должна быть квадратной'
    n = matrixShape(matrix)[0]

    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    elif n == 3:
        res = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[1][0] * matrix[2][1] * matrix[0][2] + matrix[0][
            1] * matrix[1][2] * matrix[2][0]
        res -= matrix[0][2] * matrix[1][1] * matrix[2][0] + matrix[0][0] * matrix[1][2] * matrix[2][1] + matrix[0][
            1] * matrix[1][0] * matrix[2][2]
        return res
    else:
        res = 0
        for mm in range(n):
            res += ((-1) ** mm) * (matrix[0][mm]) * det(red(matrix, 0, mm))
        return res


class Matrix(object):
    """Класс матрицы, n строк, m столбцов"""
    M = []
    detM = None


    def __init__(self, matrix):
        try:
            self.n = len(matrix)
            self.m = len(matrix[0])
        except:
            Exception("List of list expected")

        self.M = [[matrix[nn][mm] for mm in range(self.m)] for nn in range(self.n)]

    def __call__(self):
        print(*self.M, sep='\n')

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in self.M])])
        # wrong

    def shape(self):
        return self.n, self.m

    def piece(self, y, x, asList = False):
        """Возвращает матрицу с удаленной строкой y и столбцом x.
        Нужно для вычисления определителя больших матриц"""
        n, m = self.n, self.m
        res = []

        for nn in range(n):
            if nn == y: continue
            current_row = []
            for mm in range(m):
                if mm == x: continue
                current_row.append(self.M[nn][mm])
            res.append(current_row)

        if asList:
            return res
        else:
            return Matrix(res)

    def det(self):
        """Определитель матрицы"""
        if self.detM is None:
            self.detM = det(self.M)
        return self.detM

    def T(self):
        """Транспонирует матрицу, используя zip()"""

        return Matrix([list(i) for i in zip(*self.M)])

    def __add__(self, other):
        if type(other) in [float, int]:
            return Matrix([[self.M[nn][mm] + other for mm in range(self.m)] for nn in range(self.n)])
        elif type(other) == Matrix:
            assert self.n == other.n and self.m == other.m, "different sizes"
            return Matrix([[self.M[nn][mm] + other.M[nn][mm] for mm in range(self.m)] for nn in range(self.n)])

    def __sub__(self, other):
        if type(other) in ['float', 'int']:
            return Matrix([[self.M[nn][mm] - other for mm in range(self.m)] for nn in range(self.n)])
        elif type(other) == 'matrix.Matrix':
            assert self.n == other.n and self.m == other.m, "different sizes"
            return Matrix([[self.M[nn][mm] - other.M[nn][mm] for mm in range(self.m)] for nn in range(self.n)])

    # def __mult__!!

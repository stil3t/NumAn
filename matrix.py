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
    n, m = matrixShape(matrix)

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


def E(n):
    """Единичаня матрица размера n*n"""
    res = [[0 if i != j else 1 for i in range(n)] for j in range(n)]
    return Matrix(res)


def det_lst(matrix):
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
            res += ((-1) ** mm) * (matrix[0][mm]) * det_lst(red(matrix, 0, mm))
        return res


def T_lst(lst):
    """Транспонирует матрицу, используя zip()"""
    return [list(i) for i in zip(*lst)]


class Matrix(object):
    """Класс матрицы, n строк, m столбцов"""
    M = []

    def __init__(self, matrix):
        self.n, self.m = matrixShape(matrix)
        self.M = [[matrix[nn][mm] for mm in range(self.m)] for nn in range(self.n)]

    def __call__(self):
        print(*self.M, sep='\n')

    def __str__(self):
        return '\n'.join([' '.join([str(i) for i in self.M])])
        # wrong

    def shape(self):
        return self.n, self.m

    def piece(self, y, x, asList=False):
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
        return det_lst(self.M)

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
        if type(other) in [float, int]:
            return Matrix([[self.M[nn][mm] - other for mm in range(self.m)] for nn in range(self.n)])
        elif type(other) == Matrix:
            assert self.n == other.n and self.m == other.m, "different sizes"
            return Matrix([[self.M[nn][mm] - other.M[nn][mm] for mm in range(self.m)] for nn in range(self.n)])

    def __mul__(self, other):
        if type(other) in [float, int]:
            return Matrix([[self.M[nn][mm] * other for mm in range(self.m)] for nn in range(self.n)])
        elif type(other) == Matrix:
            assert self.m == other.n, "Умножение матриц невозможно"
            res = []
            for i in range(self.n):
                row = []
                for j in range(other.m):
                    x = 0
                    for z in range(self.m):
                        x += self.M[i][z] * other.M[z][j]
                    row.append(x)
                res.append(row)
            return res

    def inv(self):
        assert self.det() != 0, 'Определитель равен 0, обратная матрица не существует'
        res = Matrix([[det_lst(red(self.M, x, y)) * -((x + y) % 2 * 2 - 1) for x in range(self.m)] for y in range(self.n)])
        # чтобы избежать лишнего вызова функции транспонирования, я поменял местами аргументы функции red
        res = res * (1 / self.det())
        return res

    def Cond(self):
        """Расчет числа обсуловленности"""
        return abs(self.norm1()) * abs(self.inv().norm1())

    def add(self, B):
        """Приписывает вектор В к матрице"""
        if type(B) == list:
            B = Matrix(B).T()

        if B.n != self.n:
            B = B.T()
        assert B.n == self.n, 'Неверный размер вектора'

        for i in range(self.n):
            self.M[i].append(B.M[i][0])

        return self

    def norm1(self):
        """Рассчитывает максимум суммы модулей элементов в строке"""
        norm1 = 0
        for string in self.M:
            for index in range(len(string)):
                string[index] = abs(string[index])
            norm1 = max(norm1, sum(string))
        return norm1

    def norm2(self):
        """Рассчитывает квадратный корень из суммы квадратов элементов"""
        norm2 = 0
        for string in self.M:
            for elem in string:
                norm2 += elem ** 2
        return sqrt(norm2)
    
    def get_M(self):
        return self.M


def solve(A, B):
    """Решает матричное уравнение A*X = B"""
    assert A.n == A.m, 'Матрица А должна быть квадратной'

    return A.inv() * B


def jordan_gauss(A):
    """Решает СЛАУ методом Гаусса-Жордана"""
    A1 = A.get_M()
    for cnt in range(A.n):
        for i in range(A.n):
            d = A1[i][cnt]
            for j in range(cnt, A.m):
                if i == cnt:
                    A1[i][j] = A1[i][j] / d
        for i in range(A.n):
            d = A1[i][cnt]
            for j in range(cnt, A.m):
                if i != cnt:
                    A1[i][j] = A1[i][j] - A1[cnt][j] * d
    return A.M, A1


A = Matrix([[5, 2, 7], [2, 1, 9]]) # x1 = -11; x2 = 31
a, b = jordan_gauss(A)
print(a)
print(b)

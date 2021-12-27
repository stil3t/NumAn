import numpy as np

from matrix import *
from numpy import *
import interpolation as i
import itertools

# A = generate(3, 3)
# B = ints(3, 3)
# print(B)
# print((B.inv()))
# print(A.norm1(), A.norm2())
# print(A.Cond())
# A = Matrix([[5, 2, 7], [2, 1, 9]]) # x1 = -11; x2 = 31
# a = jordan_gauss(A)
# print(a)

# A = Matrix([[1, 2, 3],
#             [1, 0, 2],
#             [1, 0, 2]])
# B = Matrix([[3], [5], [6]])
# # C = solve(A, B)
# # print(C)
# print(jordan_gauss(A.merge(B)))

# A = Matrix([[0.000000001, 1],
#             [1, 1]])
# B = Matrix([[5], [7]])
# # print(A.Cond())
# # print(solve(A, B))
# print(jordan_gauss(A.merge(B)))


from difeqs import *
from matplotlib import pyplot as plt
from math import *

# x, y = RK4(lambda x, y: cos(x+y), 0, .4, 0, 1)
# x1, y1 = EuCau(lambda x, y: cos(x+y), 0, .4, 0, 1)
# # x, y = EuCau(lambda x, y: exp(-x)-y, 0, 1, 0, 1)
# print(Comp(y, y1))
# plt.plot(x, y)
# plt.show()
# plt.plot(x1, y1)
# plt.show()


def f1(x, y, z):
    # return x*y + z
    # return x**2 + z
    # return z**2 + x
    # return (y+z) * x
    return -y*z + cos(x)/x

def f2(x, y, z):
    # return y - z
    # return x*y
    # return (-y + z)*x
    return -z**2 + (2.5*x)/(1+x**2)


x, y = RK4s([f1, f2], 0, [1, 1])

plt.plot(x, np.transpose(y)[0])
plt.show()
plt.plot(x, np.transpose(y)[1])
plt.show()


# def f2(x, y):
#     # return exp(-x) - y
#     return x**2/x+y
#
#
# x, y = RK4(f2, 0, 1, 0, 2)
# plt.plot(x, y)
# plt.show()

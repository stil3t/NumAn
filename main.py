import matrix
from numpy import *
import interpolation as i
import itertools

# A = matrix.ints(1, 2)
# B = matrix.ints(2, 3)
# C = matrix.ints(1, 2)
# print(A)
# print(B)
# print(C)
# print(A*B)
# print(A+C)
# print(A-C)
# print(A-3)
# print(A+3)
# print(A*(-1))
# a = [[3, -2],
#      [5, 1]]
# A = matrix.Matrix(a)
# B = matrix.Matrix([[-6], [3]])
#
# print(A)
# print(B)
# # print(A.Cond())
# # print("Высеры нумпая")
# # for i in [None, 'fro', inf, -inf, 1, -1, 2, -2]:
# #     print(linalg.cond(a, i), i)
#
#
# print(A.add(B))

# i.generateDataInRange(lambda x: sin(x) - 4, 0, 8, .5, .2, buildPlot=True)

print(itertools.combinations_with_replacement([0, 0, 1, 1]))
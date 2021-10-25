import matrix
from numpy import linalg, inf
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
a = [[3, -2],
     [5, 1]]
A = matrix.Matrix(a)
B = matrix.Matrix([[-6], [3]])

print(A)
print(B)
# print(A.Cond())
# print("Высеры нумпая")
# for i in [None, 'fro', inf, -inf, 1, -1, 2, -2]:
#     print(linalg.cond(a, i), i)


print(A.add(B))

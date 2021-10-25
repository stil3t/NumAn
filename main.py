import matrix

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

A = matrix.Matrix([[3, -2],
                   [5, 1]])
B = matrix.Matrix([[-6], [3]])

print(A)
print(B)
print(matrix.solve(A, B))

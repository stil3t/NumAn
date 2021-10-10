import csv
from math import *
import numpy as np
import re

def matrixInput(fast = False):
  """Ввод матрицы пользователем.
  Сначала вводится размер, затем каждый элемент. В случае отмены, нужно ввести 'exit'.
  Также элементами могут быть строки, состоящие из букв, символа _, и цифр (но не на первой позиции)
  fast для ускоренного ввода"""

  number_of_rows = int(input("Введите число строк: "))
  number_of_elements = int(input("Введите число стобцов: "))
  matrix =[]
  
  if fast:
    for n in range(number_of_rows):
      row = [float(i) for i in input().split()]
      assert len(row) == number_of_elements, 'Неверный ввод'
      matrix.append(row)
    return matrix

  else:
    print("""Далее нужно ввести элементы матрицы.
  Первый индекс - номер строки, второй - элемент строки.
  Для выхода введите 'stop'""")
    for n in range(number_of_rows):
      row = []
      for m in range(number_of_elements):

        elem = input("a[{}][{}]".format(n, m))

        if elem=='stop':
          raise Exception('Остановлено пользователем')

        else:
          try:
            row.append(float(elem))
          except ValueError:
            assert re.fullmatch(r'[-]?[a-zA-Zа-яА-Я]', elem), 'Неверный ввод'
            row.append(elem)

      matrix.append(row)

  return matrix

def matrixGenerator(n, m, min_value = -10., max_value = 10., count = 1):
  """Функция генерирует матрицу, в которой n строк и m столбцов.
     Можно задать минимальное и максимальное значения элементов,
     сгенерировать массив из матриц"""
     
  assert min_value < max_value, 'Минимальное значение должно быть меньше максимального значения'
  
  dispersion = max_value - min_value
  x = np.random.random(n * m * count) * dispersion + min_value
  if count==1:
    x = x.reshape(n, m)
  else:
    x = x.reshape(count, n, m)

  return x

def matrixOfInts(n, m, min_value = -10, max_value = 10, count = 1):
  """Функция генерирует матрицу целых чисел, в которой n строк и m столбцов.
     Можно задать минимальное и максимальное значения элементов, сгенерировать массив из count матриц"""
  
  assert min_value < max_value, 'Минимальное значение должно быть меньше максимального значения'

  x = np.random.randint(min_value, max_value + 1, n * m * count)
  if count==1:
    x = x.reshape(n, m)
  else:
    x = x.reshape(count, n, m)

  return x

def matrixShape(matrix):
  return len(matrix), len(matrix[0])

def Transpose1(matrix):
  """Транспонирует матрицу matrix, используя генератор"""
  try:
    n, m = matrixShape(matrix)
  except:
    print('Не матрица')
  return [[matrix[x, y] for x in range(n)] for y in range(m)]

def Transpose2(matrix):
  """Транспонирует матрицу, используя zip()"""
  return [list(i) for i in zip(*matrix)]

Transpose = Transpose2
# Тесты показали, что метод, использующий zip(), быстрее
# В будущем именно он будет использоваться как основной

def red(matrix, y, x):
  """Возвращает матрицу с удаленной строкой y и столбцом x.
  Нужно для вычисления определителя больших матриц"""
  n, m = matrixShape(matrix)
  res = []

  for nn in range(n):
    if nn == y: continue
    current_row = []
    for mm in range(m):
      if mm == x: continue
      current_row.append(matrix[nn][mm])
    res.append(current_row)

  return res

def det1(matrix):
  """Нахождение определителя квадратной матрицы, рекурсия до матрицы рангом 1"""
  assert matrixShape(matrix)[0]==matrixShape(matrix)[1], 'Матрица должна быть квадратной'
  n = matrixShape(matrix)[0]

  if (n==1):
    return matrix[0][0]
  else:
    res = 0
    for mm in range(n):
      res+= ((-1)**mm)*(matrix[0][mm])*det2(red(matrix, 0, mm))
    return res

def det2(matrix):
  """Нахождение определителя квадратной матрицы, рекурсия до матрицы рангом 2"""
  assert matrixShape(matrix)[0]==matrixShape(matrix)[1], 'Матрица должна быть квадратной'
  n = matrixShape(matrix)[0]

  if (n==1):
    return matrix[0][0]
  elif (n==2):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
  else:
    res = 0
    for mm in range(n):
      res+= ((-1)**mm)*(matrix[0][mm])*det2(red(matrix, 0, mm))
    return res

def det3(matrix):
  """Нахождение определителя квадратной матрицы, рекурсия до матрицы рангом 3"""
  assert matrixShape(matrix)[0]==matrixShape(matrix)[1], 'Матрица должна быть квадратной'
  n = matrixShape(matrix)[0]

  if (n==1):
    return matrix[0][0]
  elif (n==2):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
  elif (n==3):
    res = matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[1][0]*matrix[2][1]*matrix[0][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]
    res-= matrix[0][2]*matrix[1][1]*matrix[2][0]+matrix[0][0]*matrix[1][2]*matrix[2][1]+matrix[0][1]*matrix[1][0]*matrix[2][2]
    return res
  else:
    res = 0
    for mm in range(n):
      res+= ((-1)**mm)*(matrix[0][mm])*det3(red(matrix, 0, mm))
    return res

def det4(matrix):
  """Нахождение определителя квадратной матрицы, рекурсия до матрицы рангом 4"""
  assert matrixShape(matrix)[0]==matrixShape(matrix)[1], 'Матрица должна быть квадратной'
  n = matrixShape(matrix)[0]

  if (n==1):
    return matrix[0][0]
  elif (n==2):
    return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
  elif (n==3):
    res = matrix[0][0]*matrix[1][1]*matrix[2][2]+matrix[1][0]*matrix[2][1]*matrix[0][2]+matrix[0][1]*matrix[1][2]*matrix[2][0]
    res-= matrix[0][2]*matrix[1][1]*matrix[2][0]+matrix[0][0]*matrix[1][2]*matrix[2][1]+matrix[0][1]*matrix[1][0]*matrix[2][2]
    return res
  elif (n==4):
    res = matrix[0][0]*(matrix[1][1]*matrix[2][2]*matrix[3][3]+matrix[2][1]*matrix[3][2]*matrix[1][3]+matrix[1][2]*matrix[2][3]*matrix[3][1]-matrix[1][3]*matrix[2][2]*matrix[3][1]-matrix[1][1]*matrix[2][3]*matrix[3][2]-matrix[1][2]*matrix[2][1]*matrix[3][3])
    res+= matrix[0][1]*(matrix[1][0]*matrix[2][2]*matrix[3][3]+matrix[2][0]*matrix[3][2]*matrix[1][3]+matrix[1][2]*matrix[2][3]*matrix[3][0]-matrix[1][3]*matrix[2][2]*matrix[3][0]-matrix[1][0]*matrix[2][3]*matrix[3][2]-matrix[1][2]*matrix[2][0]*matrix[3][3])
    res+= matrix[0][2]*(matrix[1][0]*matrix[2][1]*matrix[3][3]+matrix[2][0]*matrix[3][1]*matrix[1][3]+matrix[1][1]*matrix[2][3]*matrix[3][0]-matrix[1][3]*matrix[2][1]*matrix[3][0]-matrix[1][0]*matrix[2][3]*matrix[3][1]-matrix[1][1]*matrix[2][0]*matrix[3][3])
    res+= matrix[0][3]*(matrix[1][0]*matrix[2][1]*matrix[3][2]+matrix[2][0]*matrix[3][1]*matrix[1][2]+matrix[1][1]*matrix[2][2]*matrix[3][0]-matrix[1][2]*matrix[2][1]*matrix[3][0]-matrix[1][0]*matrix[2][2]*matrix[3][1]-matrix[1][1]*matrix[2][0]*matrix[3][2])
    return res
  else:
    res = 0
    for mm in range(n):
      res+= ((-1)**mm)*(matrix[0][mm])*det3(red(matrix, 0, mm))
    return res

det = det3
# Тесты времени выполнения показали, что функция det3 быстрее det1 и det2, но det4 выигрыша по времени не дает.
# Далее det3 будет использоватсья как функция по умолчанию для расчета определителя матрицы
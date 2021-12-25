from copy import deepcopy
from sys import getsizeof
import time

def determinant_fast(matryx):
    n = len(matryx)
    fresh_matryx = copy_matryx(matryx)
    for fd in range(n):
        if fresh_matryx[fd][fd] == 0:
            fresh_matryx[fd][fd] = 1.0e-18
        for i in range(fd + 1, n):
            cr_scaler = fresh_matryx[i][fd] / fresh_matryx[fd][fd]
            for j in range(n):
                fresh_matryx[i][j] = fresh_matryx[i][j] - cr_scaler * fresh_matryx[fd][j]

    product = 1.0
    for i in range(n):
        product *= fresh_matryx[i][i]

    return product

def copy_matryx(matryx):
    rows = len(matryx)
    cols = len(matryx[0])

    fresh_matryx = null_matryx(rows, cols)

    for i in range(rows):
        for j in range(cols):
            fresh_matryx[i][j] = matryx[i][j]

    return fresh_matryx

def gauss(number_of_units, matryx):
    for i in range(number_of_units):
        for j in range(number_of_units):
            if i != j:
                ratio = matryx[j][i] / matryx[i][i]
                for k in range(number_of_units + 1):
                    matryx[j][k] = matryx[j][k] - ratio * matryx[i][k]

    result_vector = []
    for i in range(number_of_units):
        vector_coord = round(matryx[i][number_of_units] / matryx[i][i], 2)
        result_vector.append(vector_coord)

    return result_vector

def null_matryx(rows, cols):
    matryx = []
    while len(matryx) < rows:
        matryx.append([])
        while len(matryx[-1]) < cols:
            matryx[-1].append(0.0)

    return matryx

def cramer(number_of_units, matryx):
    matryx_determinant = determinant_fast(matryx)
    if matryx_determinant == 0:
        raise ValueError

    result_vector = []
    for i in range(number_of_units):
        line = deepcopy(matryx)
        for j in range(number_of_units):
            line[j][i] = matryx[j][-1]
        line_determinant = round(determinant_fast(matryx=line) / matryx_determinant, 2)
        result_vector.append(line_determinant)

    return result_vector

number_of_units = int(input('Введите количество уравнений в СЛАУ: '))

time_list = []
matryx = []
for row in range(number_of_units):
    matryx_row = []
    for col in range(number_of_units + 1):
        matryx_row.append(float(input(f"Введите ненулевое значение ячейки matryx[{row}][{col}]: ")))
        matryx.append(matryx_row.copy())

    choice = input("Выберите метод для решения СЛАУ - Гаусс (1) - || - Крамер (2): ")
    start = time.time()
    if choice == "1":
        result_vector = gauss(number_of_units, matryx)
    else:
        result_vector = cramer(number_of_units, matryx)
    for i in range(number_of_units):
        print(f"X{i} = {result_vector[i]}", end='\t')
    stop = time.time()
    print(getsizeof(matryx))
    print(stop)
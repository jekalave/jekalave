from random import randint, uniform
from time import time
import matplotlib.pyplot as plt
from numpy import poly1d as np_poly1d, polyfit as np_polyfit

def matrix_multiplication_calculation(matrix_a, matrix_b):
    matrix_b = list(zip(*matrix_b))
    return [
        [
            sum(x_coord * y_coord for x_coord, y_coord in zip(matrix_a_row,
matrix_b_column))
            for matrix_b_column in matrix_b
            ]
        for matrix_a_row in matrix_a
        ]
dimension_min = 10**2
dimension_max = 10**4
dimension_step = 10**3

matrester = []
calculation_times_int = []
calculation_times_float = []
for dimension in range(dimension_min, dimension_max, dimension_step):
    matrix_a = [[randint(1, 10) for j in range(int(dimension ** 0.5))] for i in range(int(dimension**0.5))]
    matrix_b = [[randint(1, 10) for j in range(int(dimension ** 0.5))] for i in range(int(dimension ** 0.5))]

    temp = []

    for _ in range(3):
        timer_start = time()
        matrix_multiplication_calculation(matrix_a, matrix_b)
        timer_stop = time()
        temp.append(timer_stop - timer_start)

    calculation_times_int.append(sum(temp) / 3)

    temp = []

    matrix_a = [[uniform(1, 10) for j in range(int(dimension ** 0.5))] for i in range(int(dimension ** 0.5))]
    matrix_b = [[uniform(1, 10) for j in range(int(dimension ** 0.5))] for i in range(int(dimension ** 0.5))]

    for _ in range(3):
        timer_start = time()
        matrix_multiplication_calculation(matrix_a, matrix_b)
        timer_stop = time()
        temp.append(timer_stop - timer_start)

    calculation_times_float.append(sum(temp) / 3)
    matrester.append(dimension)

plt.figure(figsize=(10,6))

plt.subplot(211)
plt.plot(matrester, calculation_times_float, "o")
trend_float = np_poly1d(np_polyfit(matrester, calculation_times_float, 3))
plt.plot(matrester, trend_float(matrester), c="blue", label=f"Тренд вычислений float()")

plt.legend()
plt.xlabel("Количество элементов в списке, *10^4")
plt.ylabel("Время вычисления, с.")

plt.subplot(212)
plt.plot(matrester, calculation_times_int, "o")
trend_float = np_poly1d(np_polyfit(matrester, calculation_times_int, 3))
plt.plot(matrester, trend_float(matrester), c="red", label=f"Тренд вычислений int()")

plt.legend()
plt.xlabel("Количество элементов в списке, *10^4")
plt.ylabel("Время вычисления, с.")

plt.show()
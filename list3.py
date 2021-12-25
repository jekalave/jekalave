import time
import random
import matplotlib.pyplot as plt
from numpy import poly1d as np_poly1d, polyfit as np_polyfit

def saxpy_calculation(vector_x, vector_y, scalar_a):
    calculated_vector = [
        _x_coord * scalar_a + vector_y_coord
for vector_x_coord, vector_y_coord in zip(vector_x, vector_y)
    ]
    return calculated_vector

time_lst_int = []

n_lst_int = []
for n in range(int(10e4), int(10e5), int(10e4)):
    time_temp = 0
x_list = [random.randint(-50, 50) for point in range(n)]
y_list = [random.randint(-50, 50) for point in range(n)]
scalar = random.randint(-50, 50)
for _ in range(3):
    start = time.time()
    saxpy = saxpy_calculation(x_list, y_list, scalar)
    end = time.time()
    time_temp += end - start
time_lst_int.append(time_temp / 3)
print(time_lst_int[-1])
n_lst_int.append(int(n // 1e4))
file = open("test_results1.txt", 'a')
file.write(f'{time_lst_int[-1]:.5f}\n')
time_lst_float = []
n_lst_float = []
for n in range(int(10e4), int(10e5), int(10e4)):
    time_temp = 0
x_list = [random.uniform(-50, 50) for point in range(n)]
y_list = [random.uniform(-50, 50) for point in range(n)]
scalar = random.uniform(-50, 50)
for _ in range(3):
    start = time.time()
    saxpy = saxpy_calculation(x_list, y_list, scalar)
    end = time.time()
    time_temp += end - start
time_lst_float.append(time_temp / 3)
print(time_lst_float[-1])
n_lst_float.append(int(n//1e4))
file = open("test_results2.txt", 'a')
file.write(f'{time_lst_float[-1]:.5f}\n')

plt.plot(n_lst_float, time_lst_float, "o")
trend_float = np_poly1d(np_polyfit(n_lst_float, time_lst_float, 1))
plt.plot(n_lst_float, trend_float(n_lst_float), "r", c="blue",
label=f"Трендвычислений float()")

plt.plot(n_lst_int, time_lst_int, "o")
trend_float = np_poly1d(np_polyfit(n_lst_int, time_lst_int, 1))
plt.plot(n_lst_int, trend_float(n_lst_int), "b", c="red",
label=f"Трендвычислений int()")

plt.legend()
plt.xlabel("Количествоэлементоввсписке, *10^4")
plt.ylabel("Времявычисления, с.")

plt.show()
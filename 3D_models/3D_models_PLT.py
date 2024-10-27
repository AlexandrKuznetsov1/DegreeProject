# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time


def x(t):
    return np.cos(t)


def y(t):
    return np.sin(t)


def z(t):
    return t


t = np.linspace(0, 6*np.pi, 100)
x_vals = x(t)
y_vals = y(t)
z_vals = z(t)
start_time = time.time()
fig = plt.figure()
ax = fig.add_subplot(
    111,
    projection='3d',
)
ax.plot(
    x_vals,
    y_vals,
    z_vals,
    color='red',
)
ax.set_xlabel('X', color='green',)
ax.set_ylabel('Y', color='green',)
ax.set_zlabel('Z', color='green',)
ax.set_title('3D-модель формулы спирали PLT', color='blue')

stop_time = time.time()
result_time = round(stop_time - start_time, 2)
print(f'Время визуализации 3D модели PLT = {result_time} секунд')
plt.show()


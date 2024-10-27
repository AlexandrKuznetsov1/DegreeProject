# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import time


start_time = time.time()
plt_omega = 2
plt1 = np.linspace(0, 10, 100)
plt2 = np.cos(plt_omega * plt1)
plt3 = np.sin(plt_omega * plt1)
plt.figure(figsize=(6, 5))
plt_axis = plt.axes(projection='3d')
plt_axis.plot3D(plt2, plt3, plt1)
plt.tight_layout()
stop_time = time.time()
result_time = round(stop_time - start_time, 2)
print(f'Время построения 3D модели SNS = {result_time} секунд')
plt.show()

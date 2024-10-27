# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import time


df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';', )

a = df['year']
b = df['population']
c = df['deaths']
d = df['births']
e = df['migration']

start_time = time.time()

fig, ax = plt.subplots(figsize=(8, 5.5), layout='constrained', )
ax.plot(a, b, color='green', marker='8', linewidth=5, label='рост популяции', )
ax.plot(a, e, color='red', marker='8', linewidth=5, label='рост миграции', )
ax.set_xlabel(a.name)
ax.set_ylabel(b.name + " (млн. чел.)")
ax.set_title('Линейный график популяции и миграции населения РФ 2010-2022 год')
ax.legend(loc='best')
plt.grid()

stop_time = time.time()
result_time = round(stop_time - start_time, 2)

plt.show()
print(f'Время построения линейного графика PLT = {result_time} секунд')

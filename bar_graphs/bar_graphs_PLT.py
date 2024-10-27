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
plt.figure(figsize=(8, 5.5), )
plt.bar(a, c)
plt.bar(a, d)
plt.bar(a, e)
plt.xlabel(a.name)
plt.ylabel(c.name + ", " + d.name + ", " + e.name + " (млн. чел.)")
plt.title('столбчатая диаграмма "соотношение смертности/рождаемости/миграции"')
plt.legend(['Смертность', 'Рождаемость', 'Миграция'])

stop_time = time.time()
result_time = round(stop_time - start_time, 2)
print(f'Время построения столбчатой диаграммы PLT = {result_time} секунд')
plt.show()


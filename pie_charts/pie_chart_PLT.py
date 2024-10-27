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
population = ['Популяция', 'Умерших', 'Рожденных', 'Мигрантов']
explode = (0.2, 0, 0.1, 0.2)
wp = {'linewidth': 0.5, 'edgecolor': "yellow", }
plt.subplots(figsize=(8, 5.5), )
df[df.columns[1:]].sum().plot.pie(autopct='%1.1f%%',
                                  labels=None,
                                  explode=explode,
                                  shadow=True,
                                  startangle=55,
                                  wedgeprops=wp,
                                  textprops=dict(color="black"),
                                  title='Круговая диаграмма популяции за весь период PLT',
                                  )
plt.legend(
    population,
    loc='lower right',
    bbox_to_anchor=(1.2, 0, 0, 1),
)
stop_time = time.time()
result_time = round(stop_time - start_time, 2)
print(f'Время построения круговой диаграммы PLT = {result_time} секунд')
plt.show()

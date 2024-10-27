# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time


df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';')

a = df['year']
b = df['population']
c = df['deaths']
d = df['births']
e = df['migration']

start_time = time.time()
sns.set('paper')
sb = sns.barplot(data=df, x="year", y="deaths",)
sb1 = sns.barplot(data=df, x="year", y="births", )
sb2 = sns.barplot(data=df, x="year", y="migration", )
sb.set_title('Столбчатая диаграмма "соотношение смертности/рождаемости/миграции"')
plt.legend(['Смертность', 'Рождаемость', 'Миграция'])
plt.xlabel('Год')
plt.ylabel('Численность (млн. чел.)')

stop_time = time.time()
result_time = round(stop_time - start_time, 2)
print(f'Время построения столбчатой диаграммы SNS = {result_time} секунд')
plt.show()



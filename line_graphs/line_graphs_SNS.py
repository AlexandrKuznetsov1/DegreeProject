# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time


df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';')
sns.set()

a = df['year']
b = df['population']
c = df['deaths']
d = df['births']
e = df['migration']


# sb = sns.scatterplot(data=df, x="year", y="population")
# sb.set_title('Диаграмма рассеяния на примере популяции')
# plt.show()

start_time = time.time()
sns.lineplot(
    data=df,
    x="year",
    y='population',
    markers='O',
    color='green',
    linewidth=3,
)
sns.lineplot(
    data=df,
    x="year",
    y='migration',
    markers='O',
    color='red',
    linewidth=3,
)
sns.scatterplot(
    data=df,
    x="year",
    y="population",
    color='red',
)
plt.title('Линейный график популяции и миграции населения РФ 2010-2022 год')
plt.xlabel('Год')
plt.ylabel('Численность населения (млн. чел.)')
plt.legend(['Популяция', '', 'Миграция'])
stop_time = time.time()
result_time = round(stop_time - start_time, 2)
plt.show()
print(f'Время построения линейного графика SNS = {result_time} секунд')

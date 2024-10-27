# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time


df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';')
df.head()

a = df['year']
b = df['population']
c = df['deaths']
d = df['births']
e = df['migration']

start_time = time.time()
data = [sum(b), sum(c), sum(d), sum(e)]
explode = [0.2, 0, 0.1, 0.2]
labels = ["population", "deaths", "births", "migration"]
colors = sns.color_palette("bright")
plt.pie(
    data,
    labels=labels,
    colors=colors,
    autopct="%1.1f%%",
    explode=explode,
    shadow="True",
    startangle=30,
    textprops={"color": "black", "fontsize": 10},
    center=(0.1, 0.1),
    rotatelabels="True",
)
plt.title('Круговая диаграмма популяции за весь период SNS')
stop_time = time.time()
result_time = round(stop_time - start_time, 2)
print(f'Время построения круговой диаграммы SNS = {result_time} секунд')
plt.show()

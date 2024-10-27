# -*- coding: utf-8 -*-

import pandas as pd
import plotly.graph_objs as go
import time


df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';')
df.head()

a = df['year']
b = df['population']
c = df['deaths']
d = df['births']
e = df['migration']


start_time = time.time()
value = [b.sum(), c.sum(), d.sum(), e.sum()]
labels = [a.name, b.name, c.name, e.name]
fig = go.Figure()
fig.add_trace(go.Pie(
    values=value,
    labels=labels,
    pull=[0, 0.1, 0.15, 0.2],
    title='Кольцевая диаграмма популяции за весь период',
    rotation=55,
    hole=0.75,
    ),
)
stop_time = time.time()
result_time = round(stop_time - start_time, 2)
fig.show()
print(f'Время построения кольцевой диаграммы PX = {result_time} секунд')

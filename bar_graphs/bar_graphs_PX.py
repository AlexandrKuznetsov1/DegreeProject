# -*- coding: utf-8 -*-

import pandas as pd
import plotly.express as px
import time


df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';')
df.head()

a = df['year']
b = df['population']
c = df['deaths']
d = df['births']
e = df['migration']

start_time = time.time()
fig = px.bar(
    df,
    x=a,
    y=[c, d, e],
    template="simple_white",
)
fig.update_layout(
    xaxis_title=a.name,
    yaxis_title='Численность(млн. чел.)',
    barmode='group',
    title='Столбчатая диаграмма "соотношение смертности/рождаемости/миграции"',
    margin=dict(l=30, r=30, t=30, b=20),
)
stop_time = time.time()
time2 = round(stop_time - start_time, 2)
fig.show()
print(f'Время построения столбчатой диаграммы PX = {time2} секунд')

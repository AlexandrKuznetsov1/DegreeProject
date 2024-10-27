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
fig = go.Figure()
fig.add_trace(go.Scatter(x=a,
                         y=b,
                         mode='lines+markers',
                         name='Популяция',
                         marker=dict(color=2,
                                     colorbar=dict(title="Популяция", ),
                                     colorscale='Inferno', ),
                         )
              )
fig.add_trace(go.Scatter(x=a,
                         y=e,
                         mode='lines+markers',
                         name='Миграция', ),
              )
fig.update_layout(title='Линейный график популяции и миграции населения РФ 2010-2022 год')
fig.update_layout(xaxis_title=a.name,
                  yaxis_title=b.name + ' ' + e.name + '(млн. чел.)',
                  title={'font': dict(size=25),
                         'x': 0.5, },
                  legend_orientation="h",
                  hovermode='x',
                  )
fig.update_layout(margin=dict(l=0, r=0, t=50, b=0))
fig.update_traces(hoverinfo="all",
                  hovertemplate="Год: %{x}<br>Численность: %{y}",
                  )
stop_time = time.time()
result_time = round(stop_time - start_time, 2)
fig.show()
print(f'Время построения линейного графика PX = {result_time} секунд')

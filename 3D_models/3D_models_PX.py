# -*- coding: utf-8 -*-

import numpy as np
import plotly.graph_objs as go
import time


start_time = time.time()
t = np.linspace(0, 20, 100)
x, y, z = np.cos(t), np.sin(t), t
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            marker=dict(
                size=12,
                color=z,
                colorscale='Viridis',
                opacity=0.8,
            ),
        ),
    ],
)
fig.update_layout(title_text='3D-модель формулы спирали PX', margin=dict(l=0, r=0, b=0, t=0))

stop_time = time.time()
result_time = round(stop_time - start_time, 2)
fig.show()
print(f'Время построения 3D модели PX = {result_time} секунд')

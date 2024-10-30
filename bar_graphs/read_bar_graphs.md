# Вы находитесь в директории содержащей 3 модуля для построения Столбчатых диаграмм с использованием библиотек Matplotlib, Seaborn и Plotly
## Для построения столбчатых диаграмм использован файл data_mun_demography_123_v20240612.csv.csv содержащий общие сведения о численности населения РФ, показателях рождаемости, смертности и миграции:
![image](https://github.com/user-attachments/assets/9ea41871-c46b-443c-85fe-197fce78ff95)
## для всех графиков создан датафрейм df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';', )
## и переменные со значениями столбцов, - a = df['year'], b = df['population'], c = df['deaths'], d = df['births'], e = df['migration']
## Для фиксации времени задействован модуль time
# Matplotlib
### импортированы библиотеки matplotlib.pyplot, pandas, time. 
### Создание каркаса фигуры plt.figure(figsize=(8, 5.5), )
### для передачи координат по осям использована функция plt.bar
### Так же добавлены названия осей и графика
## [посмотреть код Matplotlib](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/bar_graphs/bar_graphs_PLT.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Столбчатая%20диаграмма%20PLT.png)
![image](https://github.com/user-attachments/assets/294e0908-7d9d-4d50-9aa8-7646bd936542)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Seaborn
### импортированы библиотеки matplotlib.pyplot, numpy, time. 
### Создание каркаса фигуры sb = sns.barplot(data=df, x="year", y="deaths",)
### для передачи координат по осям использована функция sns.barplot
### Так же добавлены названия осей и графика
## [посмотреть код Seaborn](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/bar_graphs/bar_graphs_SNS.py)____>>>>____[посмотреть реузльтат]()
![image](https://github.com/user-attachments/assets/923e029d-7256-4ffd-9074-6667fff4e950)
___________________________________________________________________________________________________________________________________________________________________________________________________________
# Plotly
### импортированы библиотеки plotly.graph_objs, numpy, time. 
### для полученияя переменных по координате z создана переменная t = np.linspace(старт 0, стоп 20, количество элементов в выходном массиве 100) 
### переменные для построения графика x, y, z = np.cos(t), np.sin(t), t
### Создание фигуры с параметрами fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(size=12, color=z, colorscale='Viridis', opacity=0.8,),),],)
### элементы Axes plt_axis = plt.axes(projection='3d'). для построения модели в ax.plot переданы полученные переменные
## [посмотреть код Plotly](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/3D_models/3D_models_PX.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/3D%20график%20РХ.png)
![image](https://github.com/user-attachments/assets/b4073a79-1ab9-4986-b4d7-99c34289778b)


# Вы находитесь в директории содержащей 3 модуля для построения Линейных графиков с использованием библиотек Matplotlib, Seaborn и Plotly
## Для построения линейных графиков использован файл data_mun_demography_123_v20240612.csv.csv содержащий общие сведения о численности населения РФ, показателях рождаемости, смертности и миграции:
![image](https://github.com/user-attachments/assets/9ea41871-c46b-443c-85fe-197fce78ff95)
## для всех графиков создан датафрейм df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';', )
## и переменные со значениями столбцов, - a = df['year'], b = df['population'], c = df['deaths'], d = df['births'], e = df['migration']
## Для фиксации времени задействован модуль time
# Matplotlib
### импортированы библиотеки matplotlib.pyplot, pandas, time. 
### Создание каркаса фигуры fig, ax = plt.subplots(figsize=(8, 5.5), layout='constrained', )
### для передачи координат по осям использована функция ax.plot
### Так же добавлены названия осей и графика с использованием ax.set
## [посмотреть код Matplotlib](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/line_graphs/line_graphs_PLT.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Линейный%20график%20PLT.png)
![image](https://github.com/user-attachments/assets/6790eb18-d839-44d1-980e-44c3a7aee6d0)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Seaborn
### импортированы библиотеки matplotlib.pyplot, pandas, time. 
### график создается с помощью нескольких слоев sns.lineplot где в качестве аргументов передается сам датафрейм, в качестве значений координат столбцы
### Так же добавлены названия осей и графика, plt.title, plt.xlabel, plt.ylabel
## [посмотреть код Seaborn]()____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Столбчатая%20диаграмма%20SNS.png)
![image](https://github.com/user-attachments/assets/77644441-63f6-4b8f-8b1d-6c2570ac1dcb)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Plotly
### импортированы библиотеки plotly.express, pandas, time. 
### Создание фигуры с параметрами fig = px.bar(df, x=a, y=[c, d, e], template="simple_white",)
### для передачи Названия графика, названий осей использован метод fig.update_layout
## [посмотреть код Plotly](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/bar_graphs/bar_graphs_PX.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Столбчатая%20диаграмма%20PX.png)
![image](https://github.com/user-attachments/assets/803a91d8-8fa0-42ca-b9a5-db2502a490cb)

